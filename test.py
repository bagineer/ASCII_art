from PIL import Image, ImageDraw, ImageFont
import numpy as np

'''
st = int("0x20", 16)
ed = int("0x7e", 16)
path = "./char_imgs/"

# 1. Set Font
fnt = ImageFont.truetype('C:/Windows/Fonts/lucon.ttf', 32)

# for i in range(st, ed+1):

i = st+3

print(chr(i), end=" ")

# 2. Create image File
new_image = Image.new("1", (20, 32))

# 3. put text into image
d = ImageDraw.Draw(new_image)
d.text((0, 0), chr(i), font=fnt, fill=1)

new_image.show()

# 4. save as image
img_name = path + "img_" + str(i) + ".png"
    # new_image.save(img_name)
'''

'''
a = np.array([[1, 2, 3, 4, 5],
              [3, 4, 5, 6, 7],
              [5, 6, 7, 8, 9],
              [2, 4, 6, 8, 10]])

print(a[1:3, 1:4])
'''


a = np.array([[0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 0]])
b = np.array([[False, False, False, False, False],
              [True, True, True, True, False],
              [True, True, True, True, False],
              [True, True, True, True, False],
              [True, True, True, True, False],
              [True, True, True, True, False],
              [True, True, True, True, False]])

img = Image.fromarray(b).convert("L")
img.show()
