# make a database from groundtruth images
# input: an image folder, output location, and database name
# output: a database at the wanted location and name
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


import utils
import compute_descriptor
from pathlib import Path

import numpy as np
import csv


# define IO details
folder = "/Users/mac/Desktop/MMA/image_folders/aaf"
db_folder = "database"
db_name = "db"

# database path
db_path = db_folder + "/" + db_name + ".txt"

# open database or create a new database if not exist
db_file = Path(db_path)
db_file.touch(exist_ok=True)

# read all images from the given folder
images = utils.read_images(folder)

data = []
# compute descriptor for each image
for item in images:
    (name, image) = item
    kp, des = compute_descriptor.sift_descriptor(image)

    data.append([name, des])
    
# save the descriptors
with open(db_path, 'w', encoding='UTF8', newline='') as f:
    
    cnt = 0 
    f.write(str(len(data)) + "\n")
    for item in data:
        name = item[0]
        desc = item[1]

        # save name and dimension of the descriptor for reading again in the future
        f.write(name + " " + str(desc.shape[0]) + " " + str(desc.shape[1]) + "\n")

        # adjust the accuracy of saving here
        np.savetxt(f, desc, fmt='%.4e')
        
        # for debuging purpose
        cnt += 1
        print("written",cnt,"/",len(data),":",name)


