from gimpfu import *


def hello_world(initstr, font, size, color):
    if font == 'Comic Sans MS':
        initstr = "Comic Sans? Are you sure?"
        img = gimp.Image(1, 1, RGB)
        pdb.gimp_context_push()
        gimp.set_foreground(color)
        layer = pdb.gimp_text_fontname(img, None, 0, 0, initstr, 10,
                                       True, size, PIXELS, font)
        img.resize(layer.width, layer.height, 0, 0)
        background = gimp.Layer(img, "Background", layer.width, layer.height, RGB_IMAGE, 100, NORMAL_MODE)
        background.fill(BACKGROUND_FILL)
        img.add_layer(background, 1)
        gimp.Display(img)
        gimp.displays_flush()
        pdb.gimp_context_pop()


register(
    "python_fu_hello_world",
    "Hello world image",
    "Create a new image with your text string",
    "myaxript",
    "myaxript",
    2018,

    "Hello world (Py)...",
    "",  # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (1.0, 0.0, 0.0))
    ],
    [],
    hello_world, menu="<Image>/File/Create")

main()
