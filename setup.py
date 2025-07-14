from setuptools import setup, find_packages

setup(
    name="pptxtoimages",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pptxtoimages = cli:main"
        ]
    },
    author="Burak Civelek",
    description="Convert .pptx presentations to image files easily.",
    keywords=["pptx", "converter", "slides", "images", "python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)