from PIL import Image
# not working since the result consequence is arbitrary
# import glob
import os
from os import path

def resizing_images(dir,size):
    files = os.listdir(dir)
    for file in files:
        file=dir+"/"+file
        outfile = path.splitext(file)[0] + ".thumbnail"
        print(outfile)
        if file != outfile:
            try:
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(outfile, "png")
            except IOError:
                print("cannot create thumbnail for '%s'" % file)

image_dir = './imgs'
size = 128,128
resizing_images(image_dir,size)