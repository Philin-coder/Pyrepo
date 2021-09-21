# TODO: and me
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

source_img = Image.open('file_name').convert("RGBA")

draw = ImageDraw.Draw(source_img)
draw.rectangle(((0, 0), (100, 100)), fill="black")

source_img.save('out_file', "JPEG")
