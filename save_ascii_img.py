from PIL import Image
import numpy as np
import pandas as pd

ROW, COL = 8, 5
MAX_SIZE = 300

def my_func(n, max_val, x):
    y = int(x / max_val * n)
    return round(y / n, 3)

src_path = "./images/"
src_name = "처신.jpg"
img = Image.open(src_path+src_name, mode="r")

n_rows, n_cols = img.size[0] // ROW, img.size[1] // COL
print(img.size)     # width, height
size = (n_rows*ROW, n_cols*COL)

scale = 1
if size[0] > MAX_SIZE:
    scale = MAX_SIZE / size[0]
    size = (int(size[0]*scale), int(size[1]*scale))
if size[1] > MAX_SIZE:
    scale = MAX_SIZE / size[1]
    size = (int(size[0]*scale), int(size[1]*scale))
print(scale)

img = img.resize(size)
print(img.size)

img = img.convert("L")
img = np.asarray(img)
print(img.shape)    # row, column

df = pd.read_csv("brightness_2.csv", index_col=0)
brightness = dict()
for v, s in zip(df['1'], df['0']):
    brightness[round(v, 3)] = str(s)
# brightness = list(zip(df['1'], df['0']))
print(brightness)

n = len(brightness)
print(n)
max_val = np.max(img)

n_rows, n_cols = img.shape[0], img.shape[1]

ascii_img = np.full((n_rows*16, n_cols*10), True, dtype=bool)
print(ascii_img.shape)

for i in range(n_rows):
    up, bottom = i*16, (i+1)*16
    for j in range(n_cols):
        left, right = j*10, (j+1)*10
        px_val = my_func(n-1, max_val, img[i, j])
        ascii_fname = "./char_imgs/img_" + brightness[px_val] + ".png"
        char_img = Image.open(ascii_fname, mode="r")
        char_img = np.asarray(char_img)
        # if i == 100 and 109< j < 111:
        #     print(char_img)
        #     print(ascii_fname)
        ascii_img[up:bottom, left:right] = char_img

ascii_img = Image.fromarray(ascii_img).convert("L")
res_path = "./results/"
img_name = "ascii_" + src_name
ascii_img.save(res_path + img_name)
