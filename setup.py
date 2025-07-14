from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pptxtoimages",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "pdf2image",
    ],
    entry_points={
        "console_scripts": [
            "pptxtoimages-cli = pptxtoimages.cli:main"
        ]
    },
    author="Burak Civelek",
    description="Convert .pptx presentations to image files easily.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords=["pptx", "converter", "slides", "images", "python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
