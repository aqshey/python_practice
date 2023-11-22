from PIL import Image
import os

def jpeg_to_pdf(input_folder, output_path):
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')]

    if not image_files:
        print("No JPEG files found in the input folder.")
        return

    with Image.open(os.path.join(input_folder, image_files[0])) as first_image:
        pdf = first_image.convert("RGB")

        for image_file in image_files[1:]:
            image_path = os.path.join(input_folder, image_file)
            with Image.open(image_path) as img:
                pdf.save(output_path, save_all=True, append_images=[img.convert("RGB")], resolution=100.0)

    print(f"PDF created successfully at {output_path}.")

if __name__ == "__main__":
    input_folder_path = "/path/to/input/folder"
    output_pdf_path = "/path/to/output/file.pdf"

    jpeg_to_pdf(input_folder_path, output_pdf_path)
