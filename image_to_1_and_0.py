# Pillow 7.0.0
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def cmyk_to_rgb(c, m, y, k, cmyk_scale, rgb_scale=255):
    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    return r, g, b



img = Image.open("javid.png")

img = img.convert('RGB')

# v = img
# value = 50
# img=np.where((255-v)<value,255,v+value) # v+value> 255 


# img.show()
WIDTH, HEIGHT = img.size

#font = ImageFont.truetype("C:/Windows/Fonts/BRITANIC.ttf", 20)
cell_width, cell_height = 8, 8

img = img.resize((int(WIDTH / cell_width), int(HEIGHT / cell_height)), Image.NEAREST)
new_width, new_height = img.size
img = img.load()

new_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
d = ImageDraw.Draw(new_img)

for i in range(new_height):

    for j in range(new_width):

        r, g, b = img[j, i]
#         r, g, b, a = img[j, i] # use this line if you have an image with alpha value
        k = int((r + g + b) / 3)
        if k < 148:
            text = "1"
        else:
            text = "0"
        d.text((j * cell_width, i * cell_height), text=text,  fill=(r, g, b))

# new_img.show()
new_img.save("sam_0_1.png")
