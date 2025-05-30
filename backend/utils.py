from rembg import remove
from PIL import Image

def process_image(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)
