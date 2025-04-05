from PIL import Image
import os

def jpgs_to_pdf(output_pdf="output.pdf", directory="."):
    # Get all .jpg files in the directory
    jpg_files = [f for f in os.listdir(directory) if f.lower().endswith(".jpg")]
    jpg_files.sort()  # Optional: sort alphabetically

    if not jpg_files:
        print("No JPG files found.")
        return

    # Open images and convert to RGB (in case some are in different modes)
    image_list = []
    for file in jpg_files:
        img_path = os.path.join(directory, file)
        img = Image.open(img_path).convert("RGB")
        image_list.append(img)

    # Save as single PDF
    first_image = image_list[0]
    remaining_images = image_list[1:]
    first_image.save(output_pdf, save_all=True, append_images=remaining_images)
    print(f"PDF created: {output_pdf}")

# Example usage
jpgs_to_pdf("combined_images.pdf", "./")
