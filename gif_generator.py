from PIL import Image
# not working since the result consequence is arbitrary
# import glob
import os
from os import path

def generate_gif(image_dir):
    imgae_num = len(os.listdir(image_dir))
    for filename in range(1,imgae_num):
        filename = str(filename) + image_format
        im = Image.open(path.join(image_dir, filename))
        image_list.append(im)

    image_list[0].save("generated.gif", save_all=True, append_images=image_list[1:])


image_list = []
image_dir = "./imgs"
image_format = '.thumbnail'

generate_gif(image_dir)