from PIL import Image

im = Image.open("test.png")
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.show()
