from pptxtoimages.tools import PPTXToImageConverter

if __name__ == "__main__":
    pptx_path = "example_file.pptx"  # Put the valid pptx file here
    output_dir = "example_output"
    output_format = "png"

    converter = PPTXToImageConverter(pptx_path, output_dir, output_format)
    result = converter.convert()

    print(f"✅ {len(result)} slide(s) converted:")
    for path in result:
        print(f" - {path}")