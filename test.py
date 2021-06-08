from PIL import Image, ImageDraw, ImageFont

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