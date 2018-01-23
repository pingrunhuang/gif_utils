from PIL import Image
# not working since the result consequence is arbitrary
# import glob
import os
from os import path

image_list = []
image_path = './imgs'
image_format = '.png'
imgae_num = len(os.listdir(image_path))
for filename in range(imgae_num):
    filename = str(filename) + image_format
    im = Image.open(path.join(image_path, filename))
    image_list.append(im)

image_list[0].save("generated.gif", save_all=True, append_images=image_list[1:])
