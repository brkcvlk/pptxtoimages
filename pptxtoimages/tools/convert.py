import subprocess
import os

class PPTXToImageConverter:
    def __init__(self, pptx_path: str, output_dir: str = "slides_images", output_format: str = "png"):
        self.pptx_path = pptx_path
        self.output_dir = output_dir
        self.output_format = output_format

    def convert(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        cmd = [
            "soffice",
            "--headless",
            "--convert-to", self.output_format,
            self.pptx_path,
            "--outdir", self.output_dir
        ]

        try:
            subprocess.run(cmd, check=True)
        except FileNotFoundError:
            raise RuntimeError(
                "LibreOffice (soffice) not found. "
                "Please install it manually:\n"
                "- Ubuntu: sudo apt install libreoffice\n"
                "- MacOS: brew install --cask libreoffice\n"
                "- Windows: https://www.libreoffice.org/download/"
            )

        output_files = sorted([
            os.path.join(self.output_dir, f)
            for f in os.listdir(self.output_dir)
            if f.lower().endswith(f".{self.output_format.lower()}")
        ])

        return output_files
