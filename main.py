import os
import sys
from PyPDF2 import PdfReader, PdfWriter, Transformation

def scale_pdf(input_path, output_path, scale_factor):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.scale_by(scale_factor)
        page.compress_content_streams()
        writer.add_page(page)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_pdf> <output_pdf> <scale_factor>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    scale_factor = float(sys.argv[3])

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    if scale_factor <= 0 or scale_factor > 1:
        print("Error: Scale factor must be between 0 and 1.")
        sys.exit(1)

    try:
        scale_pdf(input_path, output_path, scale_factor)
        print(f"PDF scaled successfully. Output saved to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
