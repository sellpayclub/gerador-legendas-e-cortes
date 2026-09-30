"""FFmpeg render: burn ASS subtitles into the video."""
from __future__ import annotations

import platform
import subprocess
import tempfile
from functools import lru_cache
from pathlib import Path
from typing import Callable, Optional

from media import ffmpeg_bin, parse_progress, escape_filter_path as _escape_filter_path

import effects as fx

FONTS_DIR = Path(__file__).resolve().parent / "fonts"


@lru_cache(maxsize=1)
def _hw_encoder_available() -> bool:
    if platform.system() != "Darwin":
        return False
    out = subprocess.run(
        [ffmpeg_bin(), "-hide_banner", "-encoders"],
        capture_output=True, text=True, check=True, timeout=30,
    )
    return "h264_videotoolbox" in out.stdout


def _ass_filter(ass_path: Path) -> str:
    ass_escaped = _escape_filter_path(ass_path.resolve().as_posix())
    if FONTS_DIR.is_dir():
        fonts_escaped = _escape_filter_path(FONTS_DIR.resolve().as_posix())
        return f"ass={ass_escaped}:fontsdir={fonts_escaped}"
    return f"ass={ass_escaped}"


def _build_video_chain(
    in_label: str,
    out_label: str,
    ass_path: Path,
    highlight_phrases: list[dict] | None,
    extras: 'ComposeExtras' | None,
    duration: float,
    canvas_w: int,
    canvas_h: int,
    headline_png: Path | None = None,
) -> str:
    current = in_label
    parts: list[str] = []

    # Blur only the source video during the dramatic phrase.  It must run
    # before ASS is burned in, otherwise the subtitle/hero phrase itself is
    # blurred as well.  The simple (no-template) renderer used to ignore
    # highlight_phrases entirely, so this effect worked only with templates.
    blur_expr = fx.blur_enable_expr(highlight_phrases) if highlight_phrases else ""
    if blur_expr:
        parts.append(
            f"[{current}]gblur=sigma=28:enable='{blur_expr}',"
            f"eq=brightness=-0.14:saturation=0.75:enable='{blur_expr}'[vblur]"
        )
        current = "vblur"

    # Burn the regular captions and the dramatic phrase after the blur.
    parts.append(f"[{current}]{_ass_filter(ass_path)}[vass]")
    current = "vass"

    if headline_png is not None and extras:
        x = max(0.0, min(1.0, extras.headline_x))
        y = extras.headline_y if extras.headline_y is not None else 0.15
        parts.append(f"[{current}][1:v]overlay=x='(W-w)*{x:.6f}':y='max(0,min(H-h,H*{y:.6f}-h/2))'[vheadline]")
        current = "vheadline"

    # progress bar fake
    if extras and extras.progress_enabled:
        from compose import _progress_overlay_chain
        from overlays import clamp_progress_height_pct
        pb_info = _progress_overlay_chain(extras, duration, canvas_w, canvas_h)
        if pb_info:
            pb_chain, x_expr = pb_info
            parts.append(pb_chain)
            h_pct = clamp_progress_height_pct(extras.progress_height_pct)
            bar_h = max(1, round(canvas_h * h_pct))
            parts.append(f"[{current}][pbar]overlay=x='{x_expr}':y={canvas_h - bar_h}[{out_label}]")
        else:
            parts.append(f"[{current}]copy[{out_label}]")
    else:
        parts.append(f"[{current}]copy[{out_label}]")

    return ";".join(parts)


def _build_cmd(
    video: Path,
    ass: Path,
    out: Path,
    hw: bool,
    duration: float,
    canvas_w: int,
    canvas_h: int,
    highlight_phrases: list[dict] | None = None,
    extras: 'ComposeExtras' | None = None,
    headline_png: Path | None = None,
) -> list[str]:
    # Highlight blur needs filter_complex even without a template or progress
    # bar. The previous condition meant the effect was silently skipped for
    # the standard subtitle export.
    use_complex = bool((extras and extras.progress_enabled) or highlight_phrases or headline_png)

    # Emit newline-delimited progress so the interface can update during long
    # renders instead of waiting for FFmpeg's final carriage-return status.
    cmd: list[str] = [ffmpeg_bin(), "-y", "-progress", "pipe:2", "-nostats", "-i", str(video)]

    if headline_png is not None:
        cmd += ["-loop", "1", "-t", f"{max(0.001, duration):.3f}", "-i", str(headline_png)]

    if use_complex:
        vchain = _build_video_chain("0:v", "vout", ass, highlight_phrases, extras, duration, canvas_w, canvas_h, headline_png)
        cmd += ["-filter_complex", vchain, "-map", "[vout]", "-map", "0:a?"]
    else:
        cmd += ["-vf", _ass_filter(ass), "-map", "0:v", "-map", "0:a?"]

    if hw:
        cmd += ["-c:v", "h264_videotoolbox", "-b:v", "8M"]
    else:
        cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20"]

    # The input may be WebM/Opus or MOV/PCM. Copying those codecs into MP4
    # produces files with poor browser/device compatibility (or fails outright).
    cmd += ["-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    return cmd


def _run_ffmpeg(
    cmd: list[str],
    duration: float,
    on_progress: Optional[Callable[[float, str], None]],
) -> tuple[int, str]:
    proc = subprocess.Popen(
        cmd, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        text=True, bufsize=1,
    )
    assert proc.stderr is not None
    stderr_tail: list[str] = []
    try:
        for line in proc.stderr:
            stderr_tail.append(line)
            if len(stderr_tail) > 40:
                stderr_tail.pop(0)
            p = parse_progress(line, duration)
            if p is not None and on_progress:
                on_progress(p, f"Renderizando... {int(p * 100)}%")
        return proc.wait(), "".join(stderr_tail)[-800:]
    finally:
        if proc.poll() is None:
            proc.kill()
        proc.stderr.close()


def render_video(
    video: Path,
    ass_path: Path,
    out_path: Path,
    duration: float,
    on_progress: Optional[Callable[[float, str], None]] = None,
    highlight_phrases: list[dict] | None = None,
    extras: 'ComposeExtras' | None = None,
    canvas_w: int = 1080,
    canvas_h: int = 1920,
) -> None:
    if not video.exists():
        raise FileNotFoundError(f"video missing: {video}")
    if not ass_path.exists():
        raise FileNotFoundError(f"ass missing: {ass_path}")
    if out_path.exists():
        out_path.unlink()

    with tempfile.TemporaryDirectory(prefix="clipshorts-headline-") as tmp:
        headline_png = None
        if extras and extras.headline_text and extras.headline_text.strip():
            from overlays import render_headline_png
            headline_png = Path(tmp) / "headline.png"
            render_headline_png(headline_png, canvas_width=canvas_w, extras=extras)
        hw = _hw_encoder_available()
        cmd = _build_cmd(video, ass_path, out_path, hw, duration, canvas_w, canvas_h, highlight_phrases, extras, headline_png)
        if on_progress:
            on_progress(0.0, f"Renderizando ({'HW' if hw else 'CPU'})...")

        rc, tail = _run_ffmpeg(cmd, duration, on_progress)
        if rc != 0 and hw:
            if out_path.exists():
                out_path.unlink()
            if on_progress:
                on_progress(0.0, "Encoder de hardware indisponível; usando CPU...")
            cpu_cmd = _build_cmd(
                video, ass_path, out_path, False, duration, canvas_w, canvas_h,
                highlight_phrases, extras, headline_png,
            )
            rc, tail = _run_ffmpeg(cpu_cmd, duration, on_progress)
        if rc != 0:
            raise RuntimeError(f"ffmpeg exited with {rc}: {tail}")
        if on_progress:
            on_progress(1.0, "Render completo")
