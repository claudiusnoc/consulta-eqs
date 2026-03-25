from rembg import remove
from PIL import Image

try:
    print("Processando imagem clara...")
    input_light = Image.open('light_raw.png')
    output_light = remove(input_light)
    output_light.save('icon_light.png')
    print("Light icon processado e salvo.")

    print("Processando imagem escura...")
    input_dark = Image.open('dark_raw.png')
    output_dark = remove(input_dark)
    output_dark.save('icon_dark.png')
    print("Dark icon processado e salvo.")
    print("Sucesso total!")
except Exception as e:
    import traceback
    traceback.print_exc()
