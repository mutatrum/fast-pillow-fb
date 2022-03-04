#!/usr/bin/env python3

import time
from PIL import Image, ImageDraw, ImageFont
from framebuffer import Framebuffer


def Main():

    fb = Framebuffer(0)

    print(fb)
    image = Image.new("RGBA", fb.size)

    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype("Roboto-Regular.ttf", 40)

    width = fb.size[0]
    height = fb.size[1]
    w3 = width / 3

    framecount = 0
    drawtime = 1
    x = y = 0
    dx = dy = 2

    while True:

        start = time.time()

        draw.rectangle(((0, 0), (w3, height)), fill="red")
        draw.rectangle(((w3, 0), (w3 * 2, height)), fill="green")
        draw.rectangle(((w3 * 2, 0), (w3 * 3, height)), fill="blue")

        text1 = "frame %d" % framecount
        draw.text(text=text1, xy=(x, y), font=fnt)
        size1 = draw.textsize(text=text1, font=fnt)

        text2 = "%.1f fps" % (1 / drawtime)
        draw.text(text=text2, xy=(x, y + size1[1]), font=fnt)
        size2 = draw.textsize(text=text2, font=fnt)

        fb.show(image)
        drawtime = (time.time() - start)
        framecount += 1

        x += dx
        y += dy

        if (x < 0) | (x > width - max(size1[0], size2[0])):
            dx = -dx
        if (y < 0) | (y > height - size1[1] - size2[1]):
            dy = -dy


if __name__ == "__main__":
    Main()
