import argparse
from pptxtoimages.tools import PPTXToImageConverter

def main():
    """
    Main function to run the pptx to images conversion example.
    Converts 'sample.pptx' into PNG images saved in 'output_images' folder.
    """
    parser = argparse.ArgumentParser(description="Convert PPTX to images")
    parser.add_argument("pptx", help="Path to the .pptx file")
    parser.add_argument("--output", default="slides_images", help="Output directory")
    parser.add_argument("--format", default="png", choices=["png", "jpg", "bmp"], help="Output image format")

    args = parser.parse_args()
    converter = PPTXToImageConverter(args.pptx, args.output, args.format)
    slides = converter.convert()
    print(f"✅ Converted {len(slides)} slides saved to {args.output}")

if __name__ == "__main__":
    main()
