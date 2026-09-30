"""Regression tests for the standard subtitle renderer."""
from pathlib import Path
import io
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from render import _build_cmd


class RenderCommandTests(unittest.TestCase):

    def test_headline_and_progress_are_independent_of_templates(self) -> None:
        from overlays import ComposeExtras

        extras = ComposeExtras(headline_text="Headline", headline_x=1, headline_y=0.75, progress_enabled=True)
        cmd = _build_cmd(Path("input.mp4"), Path("captions.ass"), Path("output.mp4"),
                         False, 1.0, 320, 240, extras=extras, headline_png=Path("headline.png"))
        graph = cmd[cmd.index("-filter_complex") + 1]
        self.assertIn("[1:v]overlay", graph)
        self.assertIn("(W-w)*1.000000", graph)
        self.assertIn("H*0.750000", graph)
        self.assertIn("[pbar]", graph)

    def test_standard_export_really_contains_headline_pixels(self) -> None:
        from PIL import Image
        from ass_gen import generate_ass
        from media import ffmpeg_bin
        from overlays import ComposeExtras
        from presets import StyleConfig
        from render import render_video

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            video, ass, output = root / "input.mp4", root / "captions.ass", root / "output.mp4"
            subprocess.run([ffmpeg_bin(), "-y", "-f", "lavfi", "-i", "color=black:s=320x240:r=25:d=0.6",
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", str(video)],
                           check=True, capture_output=True, timeout=20)
            generate_ass({"width": 320, "height": 240, "duration": 0.6, "words": []}, StyleConfig(), 3, ass)
            extras = ComposeExtras(headline_text="TEST", headline_font_size=24,
                                   headline_max_width_pct=0.5, headline_x=1, headline_y=0.75,
                                   progress_enabled=True)
            with patch("render._hw_encoder_available", return_value=False):
                render_video(video, ass, output, 0.6, extras=extras, canvas_w=320, canvas_h=240)
            frame = subprocess.run([ffmpeg_bin(), "-i", str(output), "-frames:v", "1",
                                    "-f", "image2pipe", "-vcodec", "png", "pipe:1"],
                                   check=True, capture_output=True, timeout=20).stdout
            image = Image.open(io.BytesIO(frame)).convert("RGB")
            red, green, blue = image.getpixel((300, 180))
            self.assertGreater(red, 150)
            self.assertLess(green, 80)
            self.assertLess(blue, 80)
            self.assertLess(max(image.getpixel((20, 180))), 20)

    def test_rerender_request_can_reuse_existing_captions(self) -> None:
        from main import RenderRequest

        self.assertTrue(RenderRequest(reuse_ass=True).reuse_ass)

    def test_progress_bar_is_fast_then_finishes_with_video(self) -> None:
        from overlays import fake_progress

        duration = 100.0
        # 7x through 30%, 4x through 50%, then taper to 0.3x at the end.
        self.assertAlmostEqual(fake_progress(30.0, duration), 2.10 / 3.26, places=4)
        self.assertAlmostEqual(fake_progress(50.0, duration), 2.90 / 3.26, places=4)
        self.assertAlmostEqual(fake_progress(80.0, duration), 3.20 / 3.26, places=4)
        self.assertAlmostEqual(fake_progress(100.0, duration), 1.0, places=4)
    def test_highlight_uses_blur_in_standard_export(self) -> None:
        cmd = _build_cmd(
            Path("input.mp4"), Path("captions.ass"), Path("output.mp4"),
            False, 10.0, 1080, 1920,
            [{"start": 2.0, "end": 3.0, "text": "momento"}],
        )
        self.assertIn("-filter_complex", cmd)
        graph = cmd[cmd.index("-filter_complex") + 1]
        self.assertIn("gblur", graph)
        self.assertIn("between(t,1.880,3.250)", graph)
        # The ASS subtitles are applied after the source-video blur.
        self.assertLess(graph.index("gblur"), graph.index("ass="))

    def test_plain_export_keeps_lightweight_video_filter(self) -> None:
        cmd = _build_cmd(
            Path("input.mp4"), Path("captions.ass"), Path("output.mp4"),
            False, 10.0, 1080, 1920,
        )
        self.assertIn("-vf", cmd)
        self.assertNotIn("-filter_complex", cmd)


if __name__ == "__main__":
    unittest.main()
