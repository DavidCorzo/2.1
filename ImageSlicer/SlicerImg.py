from __future__ import division
from PIL import Image
import math
import os

def get_image_size(image_path):
    img = Image.open(image_path)
    width, height = img.size
    return height

def long_slice(image_path, out_name, outdir, slice_size):
    """slice an image into parts slice_size tall"""
    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))

    count = 1
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  

        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        working_slice.save(os.path.join(outdir, "slice_" + out_name + "_" + str(count)+".png"))
        count +=1
if __name__ == '__main__':
    # width_slice = get_image_size("0001.jpg")
    # print(math.floor(width_slice))
    long_slice("0001.jpg", #image filename 
               "class", #slice names
                os.getcwd(), #output dir
                3508 #height in px
               )
