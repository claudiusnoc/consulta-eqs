import os
from rembg import remove
from PIL import Image, ImageChops

def clean_and_center(filename, output_name):
    print(f"Limpando {filename}...")
    img = Image.open(filename).convert("RGBA")
    
    # Remove background more aggressively
    # Using 'remove' directly on the original crop
    print("Chamando o rembg...")
    cleaned = remove(img)
    
    # Find bounding box of non-transparent pixels
    bbox = cleaned.getbbox()
    if bbox:
        # Crop to the object
        obj = cleaned.crop(bbox)
        
        # Create a new square canvas
        size = max(obj.width, obj.height)
        new_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        
        # Paste object in the center
        offset = ((size - obj.width) // 2, (size - obj.height) // 2)
        new_img.paste(obj, offset)
        
        # Save high-res icon
        new_img.save(output_name)
        print(f"Salvo {output_name} ({new_img.width}x{new_img.height})")
    else:
        print(f"Nenhum objeto detectado em {filename}!")

# Processar as imagens originais recortadas
clean_and_center('light_raw.png', 'icon_light.png')
clean_and_center('dark_raw.png', 'icon_dark.png')
print("Recorte e centralização concluídos!")
