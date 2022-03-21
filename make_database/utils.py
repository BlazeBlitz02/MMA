# helper functions for main

from asyncore import read
import os
import cv2
import numpy as np

# read all images from a given folder path
# input: folder path
# output a list of (name, image)
def read_images(folder_path):
    # get all image paths in the folder path
    image_names = os.listdir(folder_path)

    # read all images
    images = []
    for name in image_names:
        image_path = folder_path + "/" + name
        images.append((name, cv2.imread(image_path)))

    # return the image list
    return images
    pass


# read the database
# input: path to database
# output: a list contains [name, descriptor]
def read_database(db_path):
    res = []

    # if the database is empty
    if os.stat(db_path).st_size == 0:
        return res

    with open(db_path,'r') as f:
        # the number of descriptors
        n = int(f.readline())

        for i in range(n):
            contents = f.readline().split(" ")
            # name of the descriptor
            name = contents[0]

            # dimension of the descriptor
            row = int(contents[1])
            col = int(contents[2])

            desc = []
            for j in range(row):
                values = list(map(float, f.readline().split(" ")))
                desc.append(values)

            res.append([name, desc])


    
    return res
    pass