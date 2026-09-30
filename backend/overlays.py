"""Compose overlay helpers: extras model, fake progress, Instagram header PNG."""
from __future__ import annotations

import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    Image = None  # type: ignore[misc, assignment]
    ImageDraw = None  # type: ignore[misc, assignment]
    ImageFont = None  # type: ignore[misc, assignment]

from ass_gen import _EMOJI_CHAR_RE

FONTS_DIR = Path(__file__).resolve().parent / "fonts"


@dataclass
class InstagramHeader:
    profile_asset: str | None = None
    username: str = ""
    caption: str = ""
    bg_color: str = "#FFFFFF"
    text_color: str = "#141414"
    avatar_size: int = 72
    username_size: int = 34
    caption_size: int = 28

    @classmethod
    def from_dict(cls, d: dict | None) -> InstagramHeader | None:
        if not d:
            return None
        return cls(
            profile_asset=d.get("profile_asset"),
            username=str(d.get("username") or ""),
            caption=str(d.get("caption") or ""),
            bg_color=str(d.get("bg_color") or d.get("ig_bg_color") or "#FFFFFF"),
            text_color=str(d.get("text_color") or d.get("ig_text_color") or "#141414"),
            avatar_size=int(d.get("avatar_size") or d.get("ig_avatar_size") or 72),
            username_size=int(d.get("username_size") or d.get("ig_username_size") or 34),
            caption_size=int(d.get("caption_size") or d.get("ig_caption_size") or 28),
        )


@dataclass
class ComposeExtras:
    headline_text: str | None = None
    headline_style: str = "bold_red"
    headline_bg: str = "#E31B23"
    headline_color: str = "#FFFFFF"
    headline_font_size: int = 42
    headline_align: str = "center"
    headline_max_width_pct: float = 0.85
    headline_x: float = 0.5
    headline_y: float | None = None
    overlay_pos_x: float = 0.5
    overlay_pos_y: float = 0.5
    instagram: InstagramHeader | None = None
    logo_path: Path | None = None
    logo_x: float = 0.85
    logo_y: float = 0.78
    logo_scale: float = 0.18
    progress_enabled: bool = False
    progress_color: str = "#E31B23"
    progress_height_pct: float = 0.04

    @classmethod
    def from_dict(cls, d: dict | None, job_dir: Path | None = None) -> ComposeExtras:
        if not d:
            return cls()
        logo_path: Path | None = None
        if d.get("logo_asset") and job_dir:
            logo_path = job_dir / "assets" / Path(str(d["logo_asset"])).name
            if not logo_path.exists():
                logo_path = None
        ig_raw = d.get("instagram")
        if isinstance(ig_raw, dict):
            ig = InstagramHeader.from_dict(ig_raw)
        else:
            ig = InstagramHeader(
                profile_asset=d.get("profile_asset"),
                username=str(d.get("instagram_username") or ""),
                caption=str(d.get("instagram_caption") or ""),
                bg_color=str(d.get("ig_bg_color") or "#FFFFFF"),
                text_color=str(d.get("ig_text_color") or "#141414"),
                avatar_size=int(d.get("ig_avatar_size") or 72),
                username_size=int(d.get("ig_username_size") or 34),
                caption_size=int(d.get("ig_caption_size") or 28),
            )
        return cls(
            headline_text=d.get("headline_text") or d.get("headline"),
            headline_style=str(d.get("headline_style") or "bold_red"),
            headline_bg=str(d.get("headline_bg") or "#E31B23"),
            headline_color=str(d.get("headline_color") or "#FFFFFF"),
            headline_font_size=int(d.get("headline_font_size") or 42),
            headline_align=str(d.get("headline_align") or "center"),
            headline_max_width_pct=float(d.get("headline_max_width_pct", 0.85)),
            headline_x=max(0.0, min(1.0, float(d.get("headline_x", 0.5)))),
            headline_y=max(0.0, min(1.0, float(d["headline_y"]))) if d.get("headline_y") is not None else None,
            overlay_pos_x=float(d.get("overlay_pos_x", 0.5)),
            overlay_pos_y=float(d.get("overlay_pos_y", 0.5)),
            instagram=ig,
            logo_path=logo_path,
            logo_x=float(d.get("logo_x", 0.85)),
            logo_y=float(d.get("logo_y", 0.78)),
            logo_scale=float(d.get("logo_scale", 0.18)),
            progress_enabled=bool(d.get("progress_enabled", False)),
            progress_color=str(d.get("progress_color") or "#E31B23"),
            progress_height_pct=float(d.get("progress_height_pct", 0.04)),
        )


def clamp_progress_height_pct(pct: float) -> float:
    return max(0.02, min(0.12, float(pct)))


def headline_box_border(style: str) -> int:
    return 24 if style == "bold_red" else 8


def headline_box_radius(style: str) -> int:
    return 14 if style == "bold_red" else 10


def headline_font_size(size: int | None) -> int:
    return max(20, min(80, int(size or 42)))


def headline_display_text(text: str, style: str) -> str:
    """Uppercase for bold_red but never mutate emoji codepoints."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if style != "bold_red":
        return normalized

    def upper_part(segment: str) -> str:
        out: list[str] = []
        last = 0
        for m in _EMOJI_CHAR_RE.finditer(segment):
            if m.start() > last:
                out.append(segment[last : m.start()].upper())
            out.append(m.group(0))
            last = m.end()
        if last < len(segment):
            out.append(segment[last:].upper())
        return "".join(out)

    return "\n".join(upper_part(p) for p in normalized.split("\n"))


def _text_width(draw: ImageDraw.ImageDraw, text: str, font: Any) -> float:
    try:
        return float(draw.textlength(text or " ", font=font))
    except AttributeError:
        bbox = font.getbbox(text or " ")
        return float(bbox[2] - bbox[0])


def _headline_line_width(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: Any,
    emoji_font: Any,
    emoji_h: int,
) -> float:
    width = 0.0
    last = 0
    for m in _EMOJI_CHAR_RE.finditer(text):
        if m.start() > last:
            width += _text_width(draw, text[last : m.start()], font)
        em = m.group(0)
        glyph = _emoji_glyph(em, emoji_font, emoji_h)
        width += float(glyph[1] if glyph else _text_width(draw, em, font))
        last = m.end()
    if last < len(text):
        width += _text_width(draw, text[last:], font)
    return width


def _draw_headline_line(
    draw: ImageDraw.ImageDraw,
    img: Any,
    x: int,
    y: int,
    text: str,
    font: Any,
    emoji_font: Any,
    fill: tuple[int, int, int],
    emoji_h: int,
) -> None:
    cursor = float(x)
    last = 0
    label = text if text else " "
    for m in _EMOJI_CHAR_RE.finditer(label):
        if m.start() > last:
            seg = label[last : m.start()]
            draw.text((cursor, y), seg, font=font, fill=fill, anchor="ls")
            cursor += _text_width(draw, seg, font)
        em = m.group(0)
        glyph = _emoji_glyph(em, emoji_font, emoji_h)
        if glyph:
            patch, nw = glyph
            paste_y = int(y - emoji_h)
            img.paste(patch, (int(cursor), paste_y), patch)
            cursor += nw
        else:
            draw.text((cursor, y), em, font=font, fill=fill, anchor="ls")
            cursor += _text_width(draw, em, font)
        last = m.end()
    if last < len(label):
        seg = label[last:]
        draw.text((cursor, y), seg, font=font, fill=fill, anchor="ls")


def _line_ascent_descent(font: Any, emoji_font: Any) -> tuple[int, int]:
    a1, d1 = font.getmetrics()
    # Emoji font is loaded at a massive fixed size and scaled down during drawing,
    # so we should not include its unscaled metrics in the line height calculation.
    return a1, d1


def layout_headline_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: Any,
    max_width_px: int,
    emoji_font: Any | None = None,
    emoji_h: int | None = None,
) -> list[str]:
    """Word-wrap per paragraph; preserve explicit newlines from the user."""
    ef = emoji_font or font
    eh = emoji_h or _emoji_target_height(font)
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines: list[str] = []
    for paragraph in normalized.split("\n"):
        if paragraph == "":
            lines.append("")
            continue
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = ""
        for word in words:
            trial = f"{current} {word}".strip() if current else word
            trial_w = _headline_line_width(draw, trial, font, ef, eh)
            if trial_w <= max_width_px or not current:
                current = trial
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines if lines else [normalized]


def wrap_headline_text(
    text: str,
    canvas_width: int,
    font_size: int,
    width_pct: float = 0.85,
) -> str:
    """Legacy helper — prefer render_headline_png for export."""
    if Image is None or ImageDraw is None:
        pct = max(0.5, min(1.0, width_pct))
        max_chars = max(6, int(canvas_width * pct / max(6.0, font_size * 0.55)))
        lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        out: list[str] = []
        for para in lines:
            if not para:
                out.append("")
                continue
            wrapped = textwrap.wrap(para, width=max_chars, break_long_words=False)
            out.extend(wrapped if wrapped else [para])
        return "\n".join(out)

    fs = headline_font_size(font_size)
    font = _load_font(fs, bold=True)
    scratch = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(scratch)
    max_w = int(canvas_width * max(0.5, min(1.0, width_pct)))
    return "\n".join(layout_headline_lines(draw, text, font, max_w))


def render_headline_png(
    out_path: Path,
    *,
    canvas_width: int,
    extras: ComposeExtras,
) -> Path:
    """Render headline as RGBA PNG — pixel-accurate WYSIWYG with preview."""
    if Image is None or ImageDraw is None:
        raise RuntimeError("Pillow não instalado — pip install pillow")

    raw_text = (extras.headline_text or "").strip()
    if not raw_text:
        raise ValueError("headline vazia")

    style = extras.headline_style or "bold_red"
    display = headline_display_text(raw_text, style)
    fs = headline_font_size(extras.headline_font_size)
    border = headline_box_border(style)
    bg_hex = extras.headline_bg if style == "bold_red" else (extras.headline_bg or "#000000")
    fg_hex = extras.headline_color or "#FFFFFF"
    align = extras.headline_align or "center"
    max_w = int(canvas_width * max(0.5, min(1.0, extras.headline_max_width_pct)))
    content_w = max(20, max_w - border * 2)

    font = _load_font(fs, bold=(style == "bold_red"))
    emoji_font = _load_emoji_font(fs)
    emoji_h = _emoji_target_height(font)
    measure = Image.new("RGBA", (max_w + border * 4, 5000), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(measure)
    lines = layout_headline_lines(mdraw, display, font, content_w, emoji_font, emoji_h)

    # Mimic CSS line-height: 1.1 and baseline positioning
    line_h = int(fs * 1.1)
    content_h = line_h * max(1, len(lines))
    baseline_offset = int(fs * 0.8)
    
    content_w = max(20, max_w - border * 2)
    total_w = content_w + border * 2
    total_h = content_h + border * 2

    bg = _hex_to_rgb(bg_hex)
    fg = _hex_to_rgb(fg_hex)
    img = Image.new("RGBA", (max(1, total_w), max(1, total_h)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = headline_box_radius(style)
    draw.rounded_rectangle((0, 0, total_w, total_h), radius=radius, fill=(*bg, 255))

    y = border + baseline_offset
    for line in lines:
        if line.strip():
            lw = int(_headline_line_width(draw, line if line else " ", font, emoji_font, emoji_h))
            if align == "left":
                x = border
            elif align == "right":
                x = total_w - border - lw
            else:
                x = border + max(0, (content_w - lw) // 2)

            _draw_headline_line(draw, img, x, y, line, font, emoji_font, fg, emoji_h)
        y += line_h

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")
    return out_path


def fake_progress(t: float, duration: float) -> float:
    """Return front-loaded bar fill 0..1, ending exactly with the video."""
    if duration <= 0:
        return 0.0
    if t >= duration:
        return 1.0
    ratio = max(0.0, t / duration)
    # Perceived velocity: 7x for the first 30%, then 4x until 50%, 1x until
    # 80%, and 0.3x to the end. Normalize the segments so the last pixel
    # reaches the edge exactly as the video ends.
    total = 7.0 * 0.30 + 4.0 * 0.20 + 1.0 * 0.30 + 0.3 * 0.20
    first = 7.0 * 0.30 / total
    second = (7.0 * 0.30 + 4.0 * 0.20) / total
    third = (7.0 * 0.30 + 4.0 * 0.20 + 1.0 * 0.30) / total
    if ratio <= 0.30:
        return min(1.0, ratio / 0.30 * first)
    if ratio <= 0.50:
        return min(1.0, first + (ratio - 0.30) / 0.20 * (second - first))
    if ratio <= 0.80:
        return min(1.0, second + (ratio - 0.50) / 0.30 * (third - second))
    return min(1.0, third + (ratio - 0.80) / 0.20 * (1.0 - third))


def fake_progress_expr(duration: float) -> str:
    """FFmpeg expression for progress fraction 0..1 (use with scale/overlay; drawbox has no time t)."""
    d = max(0.001, duration)
    total = 7.0 * 0.30 + 4.0 * 0.20 + 1.0 * 0.30 + 0.3 * 0.20
    first = 7.0 * 0.30 / total
    second = (7.0 * 0.30 + 4.0 * 0.20) / total
    third = (7.0 * 0.30 + 4.0 * 0.20 + 1.0 * 0.30) / total
    t1, t2, t3 = (d * 0.30, d * 0.50, d * 0.80)
    inner = (
        f"if(lt(t,{t1:.3f}),t/({t1:.3f})*{first:.6f},"
        f"if(lt(t,{t2:.3f}),{first:.6f}+(t-{t1:.3f})/({t2 - t1:.3f})*{second - first:.6f},"
        f"if(lt(t,{t3:.3f}),{second:.6f}+(t-{t2:.3f})/({t3 - t2:.3f})*{third - second:.6f},"
        f"{third:.6f}+(t-{t3:.3f})/({d - t3:.3f})*{1.0 - third:.6f})))"
    )
    return f"min(1,{inner})"


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _load_font(size: int, bold: bool = False) -> Any:
    if ImageFont is None:
        raise RuntimeError("Pillow não instalado — pip install pillow")
    names = ["Roboto-Bold.ttf", "Inter-Bold.ttf"] if bold else ["Roboto-Regular.ttf", "OpenSans-Regular.ttf"]
    for name in names:
        p = FONTS_DIR / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


EMOJI_FONT_PX = 109


def _load_emoji_font(_size: int) -> Any:
    if ImageFont is None:
        raise RuntimeError("Pillow não instalado — pip install pillow")
    p = FONTS_DIR / "NotoColorEmoji.ttf"
    if p.exists():
        return ImageFont.truetype(str(p), EMOJI_FONT_PX)
    return _load_font(_size, bold=False)


def _emoji_target_height(text_font: Any) -> int:
    ascent, _ = text_font.getmetrics()
    return max(1, ascent)


def _emoji_glyph(emoji: str, emoji_font: Any, target_h: int) -> tuple[Any, int] | None:
    if Image is None:
        return None
    scratch = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scratch)
    sd.text((8, 8), emoji, font=emoji_font, fill=(255, 255, 255, 255), anchor="lt")
    bbox = scratch.getbbox()
    if not bbox:
        return None
    crop = scratch.crop(bbox)
    nh = max(1, target_h)
    nw = max(1, round(crop.width * (nh / max(1, crop.height))))
    return crop.resize((nw, nh), Image.Resampling.LANCZOS), nw


def render_instagram_header_png(
    out_path: Path,
    *,
    width: int,
    height: int,
    username: str,
    caption: str,
    profile_path: Path | None = None,
    bg_color: str = "#FFFFFF",
    text_color: str = "#141414",
    avatar_size: int = 72,
    username_size: int = 34,
    caption_size: int = 28,
) -> Path:
    """Render white Instagram-style header as PNG."""
    if Image is None:
        raise RuntimeError("Pillow não instalado — pip install pillow")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    bg = _hex_to_rgb(bg_color)
    fg = _hex_to_rgb(text_color)
    img = Image.new("RGBA", (width, height), (*bg, 255))
    draw = ImageDraw.Draw(img)

    avatar_d = max(40, min(96, avatar_size))
    ax, ay = 36, 36
    if profile_path and profile_path.exists():
        try:
            av = Image.open(profile_path).convert("RGBA")
            av = av.resize((avatar_d, avatar_d), Image.Resampling.LANCZOS)
            mask = Image.new("L", (avatar_d, avatar_d), 0)
            ImageDraw.Draw(mask).ellipse((0, 0, avatar_d, avatar_d), fill=255)
            img.paste(av, (ax, ay), mask)
        except Exception:
            draw.ellipse((ax, ay, ax + avatar_d, ay + avatar_d), fill=(220, 220, 220))
    else:
        draw.ellipse((ax, ay, ax + avatar_d, ay + avatar_d), fill=(220, 220, 220))

    user_font = _load_font(max(18, username_size), bold=True)
    cap_font = _load_font(max(14, caption_size), bold=False)
    uname = username.strip() or "usuario"
    draw.text((ax + avatar_d + 20, ay + 8), uname, fill=fg, font=user_font)

    for i, dy in enumerate((0, 14, 28)):
        draw.ellipse((width - 48, ay + 18 + dy, width - 40, ay + 26 + dy), fill=(80, 80, 80))

    cap_y = ay + avatar_d + 24
    cap_text = caption.strip() or "Sua legenda aqui..."
    wrapped = textwrap.fill(cap_text, width=42)
    draw.multiline_text((36, cap_y), wrapped, fill=fg, font=cap_font, spacing=6)

    img.convert("RGB").save(out_path, "PNG")
    return out_path


def escape_drawtext(text: str) -> str:
    """Escape text for FFmpeg drawtext filter."""
    out = []
    for ch in text:
        if ch in "\\':%":
            out.append("\\" + ch)
        elif ch == "\n":
            out.append("\n")
        else:
            out.append(ch)
    return "".join(out)
