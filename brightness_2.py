from PIL import Image
import os
import numpy as np
import pandas as pd

path = "./char_imgs/"

# repeated = [41, 92, 62, 93, 125, 45, 39, 95, 126, 59, 42, 124, 60,
# 47, 61, 105, 114, 76, 74, 118, 99, 40, 84, 63, 89, 116, 123, 115, 70,
# 120, 73, 122, 49, 67, 121, 86, 106, 53, 50, 102, 110, 117, 88, 90, 85,
# 83, 80, 65, 75, 111, 97, 101, 69, 107, 119, 71, 104, 36, 82, 68, 109, 113,
# 37, 78, 112, 35, 48, 57, 98, 100, 77, 66, 87, 81, 103]
# repeated = list(map(str, repeated))
# print(repeated)

brightness = list()
min_val, norm = 0.68615625, 0.31384375

tmp_list = []  #
img_list = os.listdir(path)

for _img in img_list:
    img = Image.open(path + _img, "r")
    val = np.asarray(img)

    _, tmp = _img.split("_")
    n, _ = tmp.split(".")

    avg = np.average(val)
    avg = (avg - min_val) / norm
    brightness.append((str(n), avg))
    tmp_list.append(np.average(val))  #

print(min(tmp_list), max(tmp_list))  #
print(max(tmp_list) - min(tmp_list))  #

brightness.sort(key=lambda x: x[1])
print(brightness)

k = len(brightness) - 1
new_bright = []

for i in range(k):
    new_bright.append((brightness[i][0], round(i / k, 3)))
new_bright.append((brightness[-1][0], 1))

print(new_bright)

df = pd.DataFrame(new_bright)
print(df)

df.to_csv("brightness_2.csv", mode="w")
