from PIL import Image
import numpy as np
import pandas as pd

ROW, COL = 8, 5
MAX_SIZE = 300

def my_func(n, max_val, x):
    y = int(x / max_val * n)
    return round(y / n, 3)


img = Image.open("./images/864768_597958_1134.jpg", mode="r")

n_rows, n_cols = img.size[0] // ROW, img.size[1] // COL
print(img.size)
size = (n_rows*ROW, n_cols*COL)

scale = 1
if size[0] > MAX_SIZE:
    scale = MAX_SIZE / size[0]
    size = (int(size[0]*scale), int(size[1]*scale))
if size[1] > MAX_SIZE:
    scale = MAX_SIZE / size[1]
    size = (int(size[0]*scale), int(size[1]*scale))
print(scale)
# size = (int(size[0]*scale), int(size[1]*scale))

img = img.resize(size)
print(img.size)

# img.show()

img = img.convert("L")
img = np.asarray(img)
f = open("./results/result.txt", "w")
print(img.shape)

# n_rows, n_cols = img.shape[0] // ROW, img.shape[1] // COL

df = pd.read_csv("brightness_2.csv", index_col=0)
brightness = dict()
for v, s in zip(df['1'], df['0']):
    brightness[round(v, 3)] = chr(s)
# brightness = list(zip(df['1'], df['0']))
print(brightness)

n = len(brightness)
print(n)
max_val = np.max(img)

n_rows, n_cols = img.shape

for i in range(n_rows):
    # up, bottom = ROW*i, ROW*(i+1)
    # if bottom >= img.shape[0]:
    #     break
    for j in range(n_cols):
        # left, right = COL*j, COL*(j+1)
        # if right >= img.shape[1]:
        #     break
        # px_avg = np.average(img[up:bottom, left:right])
        px_avg = np.average(img[i, j])
        px_val = my_func(n-1, max_val, px_avg)
        f.write(brightness[px_val])
    f.write("\n")

f.close()

# img.show()