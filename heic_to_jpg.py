import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

for filename in os.listdir('.'):
    if filename.lower().endswith('.heic'):
        try:
            output_name = os.path.splitext(filename)[0] + '.jpg'
            with Image.open(filename) as img:
                img.convert('RGB').save(output_name, 'JPEG')
            print(f"Successfully converted: {filename} -> {output_name}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
