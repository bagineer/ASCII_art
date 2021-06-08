from PIL import Image
import numpy as np
import pandas as pd

ROW, COL = 1, 1

def my_func(n, max_val, x):
    y = int(x / max_val * n)
    return round(y / n, 3)

img = Image.open("./images/unnamed.jpg", mode="r")
img = img.convert("L")
img = np.asarray(img)
f = open("./results/result.txt", "w")
print(img.shape)

n_rows, n_cols = img.shape[0] // ROW, img.shape[1] // COL

df = pd.read_csv("brightness_1.csv", index_col=0)
brightness = dict()
for v, s in zip(df['1'], df['0']):
    brightness[round(v, 3)] = chr(s)
# brightness = list(zip(df['1'], df['0']))
print(brightness)

n = len(brightness)
print(n)
max_val = np.max(img)

for i in range(n_rows):
    for j in range(n_cols):
        px_val = my_func(n-1, max_val, img[i][j])
        f.write(brightness[px_val])
    f.write("\n")

f.close()

print(img.shape)

# img.show()