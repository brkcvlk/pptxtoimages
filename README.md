# pptxtoimages

[![PyPI version](https://img.shields.io/pypi/v/pptxtoimages.svg)](https://pypi.org/project/pptxtoimages/)
[![Downloads](https://static.pepy.tech/badge/pptxtoimages)](https://pepy.tech/project/pptxtoimages)
[![License](https://img.shields.io/github/license/brkcvlk/pptxtoimages.svg)](LICENSE)

## Overview

**pptxtoimages** is a lightweight Python package to convert `.pptx` PowerPoint presentations into high-quality image files (PNG by default).  
It uses LibreOffice (`soffice`) to convert `.pptx` files to PDF, then converts PDF pages to images using `pdf2image`.  

This project aims to provide an easy-to-use, open-source tool for developers who need to quickly generate slide images from PowerPoint files for further processing, presentations, or video creation.

---

## Features

- Convert `.pptx` slides to images automatically  
- Output images saved in PNG format by default  
- Supports batch processing of multi-slide presentations  
- Cross-platform support (Windows, Linux, macOS) with LibreOffice installed  
- CLI support for quick command line usage  

---

## Installation

Make sure you have the following prerequisites installed:

- [LibreOffice](https://www.libreoffice.org/) (`soffice` command available in your system PATH)  
- [Poppler](https://poppler.freedesktop.org/) utilities installed (`poppler-utils` on Linux)

Then install the package via pip:

```bash
    pip install pptxtoimages
```
---

## Usage
### Python

```
    from pptxtoimages.tools import PPTXToImageConverter

    # Initialize converter
    converter = PPTXToImageConverter(pptx_path)

    # Convert your .pptx file to images
    images = converter.convert("path/to/presentation.pptx", output_dir="output_images")

    print(f"Converted {len(images)} slides to images.")
```

### Command Line Interface (CLI)
Convert a pptx file directly from the terminal :

```
    pptxtoimages-cli path/to/presentation.pptx --output output_images
```

Note : For more examples and details, please check the ```example.py``` file.



---

## Configuration 
- Output image format is PNG by default, but can be customized in the Converter class parameters.

- Output directory will be created if it does not exist.

## Development

#### To contribute or develop locally:

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies:
```
    pip install -r requirements.txt
```
4. Install pre-commit hooks (optional but recommended)
    - This ensures your code is auto-formatted (e.g., by black) before each commit.
###  Versioning
- You may use `bump2version` to suggest version changes only if authorized by the project maintainer.
Please respect versioning boundaries – we welcome contributions, but all official releases are maintained and approved manually by the maintainer.

6. Open a pull request

---
## Links

- **[Download on PyPI](https://pypi.org/project/pptxtoimages/)**
- **[View Download Stats](https://pepy.tech/project/pptxtoimages)**
- **[View Source on GitHub](https://github.com/brkcvlk/pptxtoimages)**
- **[Report Issues](https://github.com/brkcvlk/pptxtoimages/issues)**

## Support This Project
If you find pptxtoimages helpful or useful, please consider giving it a star on GitHub!
Your support helps the project grow and motivates further development.

- **[Star this project on GitHub](https://github.com/brkcvlk/pptxtoimages)**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact

Created by Burak Civelek

Feel free to reach out for questions or suggestions!



