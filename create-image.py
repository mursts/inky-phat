#!/usr/bin/env python
# coding: utf-8

import os
import random

from PIL import Image
from inky import InkyPHAT

PALLETE_SIZE = (212, 104)
PALLETE_COLOR = (255, 255, 255)


def main():
    im = Image.new('RGB', PALLETE_SIZE, PALLETE_COLOR)
    base_w, base_h = im.size

    file_name = str(random.choice(range(252))) + '.png'
    image_file = os.path.join(os.path.dirname(__file__), 'images', file_name)

    base_img = Image.open(image_file)
    base_img = base_img.resize((104, 104))

    w, h = base_img.size
    im.paste(base_img, (int(base_w / 2 - w / 2), int(base_h / 2 - h / 2)))

    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=3)
    im.putpalette([255, 255, 255,
                   0, 0, 0,
                   255, 0, 0,
                   ])

    inky_display = InkyPHAT('black')
    inky_display.set_border(inky_display.BLACK)

    inky_display.set_image(im)
    inky_display.show()


if __name__ == '__main__':
    main()
