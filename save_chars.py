from PIL import Image, ImageDraw, ImageFont

st = int("0x20", 16)
ed = int("0x7e", 16)
path = "./char_imgs/"
scaler = 20  # (5, 8), (7, 4), (8, 3), (9, 3), (10, 5), (11, 3)

repeated = [41, 92, 62, 93, 125]
ascii_list = [i for i in range(st, ed+1) if i not in repeated]

print(ascii_list)

# 1. Set Font
fnt = ImageFont.truetype('C:/Windows/Fonts/lucon.ttf', 16*scaler)  # 16

for i in ascii_list:
    print(chr(i), end=" ")

    # 2. Create image File
    new_image = Image.new("1", (10*scaler, 16*scaler))    # (10, 16)

    # 3. put text into image
    d = ImageDraw.Draw(new_image)
    d.text((0, 0), chr(i), font=fnt, fill=1)

    # 4. save as image
    img_name = path + "img_" + str(i) + ".png"
    new_image.save(img_name)