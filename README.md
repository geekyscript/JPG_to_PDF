
# 🖼️ Convert JPG Images to a PDF with Python in Seconds! 🐍

Want to convert multiple JPG images into a single PDF without using any online tools? This simple and powerful Python script lets you automate the process in seconds using the `Pillow` library!

---

## 📌 Why This Tutorial?

- ✅ No internet needed — works offline!
- ✅ Batch convert multiple images
- ✅ Perfect for scanned documents, handwritten notes, or portfolios
- ✅ Beginner-friendly automation project

---

## 🛠️ Prerequisites

Make sure you have Python installed. Then install the `Pillow` library:

```bash
pip install Pillow
```

---

## 🧠 The Python Script

```python
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
```

---

## 📂 Output

The script will generate a single PDF file named `combined_images.pdf` from all `.jpg` images found in the specified directory.

---

## 💡 Tips & Customizations

- You can change the `directory` parameter to scan a different folder.
- Sort your image files properly if order matters.
- You can extend this to support PNG files too — just tweak the filter!

---

## 🔚 Final Thoughts

This project is a fantastic way to get started with **Python automation** and **image processing**. You now have your own image-to-PDF converter ready to go, and you can expand this into a full-fledged app with a GUI later on!

---

### 🔖 Tags

`python`, `jpg to pdf`, `image converter`, `pdf`, `python automation`, `pillow`, `python project`, `beginner python`, `python tutorial`, `convert jpg to pdf`, `image processing`

---

👍 Liked this tutorial? Share it with your fellow coders and keep building cool stuff with Python!
