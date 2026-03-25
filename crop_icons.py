from PIL import Image
import os

img_path = r"C:\Users\Claudius\Downloads\Gemini_Generated_Image_5azlnv5azlnv5azl.png"

if not os.path.exists(img_path):
    print(f"Error: Could not find image at {img_path}")
    exit(1)

img = Image.open(img_path)
width, height = img.size

# Crop the left and right halves
margin = 50 # Add a margin to avoid catching edges from the other side if they are close
left_crop = img.crop((0, 0, width // 2, height))
right_crop = img.crop((width // 2, 0, width, height))

left_crop.save("light_raw.png")
right_crop.save("dark_raw.png")
print("Saved light_raw.png and dark_raw.png")
