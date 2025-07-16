"""
example.py

This script demonstrates how to use the pptxtoimages package to convert
a .pptx PowerPoint presentation file into image files.

It shows:
- How to import the Converter class,
- How to convert a pptx file to images,
- How to handle output directory and file naming.

Output:
- Images are saved in PNG format by default.
- Output format can be customized in the Converter class parameters.

Requirements:
- 'soffice' (LibreOffice) must be installed and available in system PATH to convert pptx to pdf.
- 'poppler' must be installed (e.g. poppler-utils on Linux) for pdf2image to convert pdf pages to images.

Usage:
    python example.py

Author: Burak Civelek
"""
from pptxtoimages.tools import PPTXToImageConverter

if __name__ == "__main__":
    pptx_path = "example_file.pptx"
    output_dir = "example_output"
    output_format = "png"

    converter = PPTXToImageConverter(pptx_path, output_dir, output_format)
    result = converter.convert()

    print(f"✅ {len(result)} slide(s) converted:")
    for path in result:
        print(f" - {path}")
