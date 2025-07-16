import subprocess
import os
import shutil

try:
    from pdf2image import convert_from_path
except ImportError:
    convert_from_path = None


class PPTXToImageConverter:
    """
    Converts a PPTX file into individual slide images (PNG, JPG, etc.)

    This class uses LibreOffice (soffice) to convert the PPTX to PDF,
    then converts each PDF page to an image using pdf2image.

    Requirements:
        - LibreOffice installed and accessible via 'soffice' command
        - Poppler utils installed (pdftoppm)
        - pdf2image Python package installed

    Args:
        pptx_path (str): Path to the input PPTX file.
        output_dir (str): Directory to save output images. Defaults to 'slides_images'.
        output_format (str): Image format to save (png, jpg, etc.). Defaults to 'png'.
        temp_dir (str): Temporary directory to store intermediate files. Defaults to 'temp'.

    Raises:
        RuntimeError: If LibreOffice (soffice) is not found.
        ImportError: If pdf2image is not installed.
        EnvironmentError: If Poppler utils are not installed.
        FileNotFoundError: If the PDF file is not created after conversion.
    """

    def __init__(
        self,
        pptx_path: str,
        output_dir: str = "slides_images",
        output_format: str = "png",
        temp_dir: str = "temp",
    ):
        self.pptx_path = pptx_path
        self.output_dir = output_dir
        self.output_format = output_format.lower()
        self.temp_dir = temp_dir

        if convert_from_path is None:
            raise ImportError(
                "pdf2image package is not installed. Please install it with 'pip install pdf2image'."
            )

        if not self._check_poppler_installed():
            raise EnvironmentError(
                "Poppler utils not found. Please install poppler.\n"
                "- Ubuntu/Debian: sudo apt install poppler-utils\n"
                "- MacOS: brew install poppler\n"
                "- Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases and add to PATH"
            )

    def _check_poppler_installed(self):
        from shutil import which

        return which("pdftoppm") is not None

    def _convert_pptx_to_pdf(self):
        """Convert the PPTX file to a PDF using LibreOffice (soffice)."""
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        cmd = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            self.pptx_path,
            "--outdir",
            self.temp_dir,
        ]
        try:
            subprocess.run(
                cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except FileNotFoundError:
            raise RuntimeError(
                "LibreOffice (soffice) not found. "
                "Please install it manually:\n"
                "- Ubuntu: sudo apt install libreoffice\n"
                "- MacOS: brew install --cask libreoffice\n"
                "- Windows: https://www.libreoffice.org/download/"
            )
        pdf_filename = os.path.splitext(os.path.basename(self.pptx_path))[0] + ".pdf"
        pdf_path = os.path.join(self.temp_dir, pdf_filename)
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"PDF file not found after conversion: {pdf_path}")
        return pdf_path

    def _convert_pdf_to_images(self, pdf_path):
        """Convert each page of the PDF into separate images using pdf2image."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        pages = convert_from_path(pdf_path, dpi=200)
        output_files = []
        for i, page in enumerate(pages):
            output_file = os.path.join(
                self.output_dir, f"slide_{i+1}.{self.output_format}"
            )
            page.save(output_file, self.output_format.upper())
            output_files.append(output_file)
        return output_files

    def convert(self):
        """Performs the full conversion from PPTX to images and cleans temp files."""
        pdf_path = self._convert_pptx_to_pdf()
        images = self._convert_pdf_to_images(pdf_path)
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        return images
