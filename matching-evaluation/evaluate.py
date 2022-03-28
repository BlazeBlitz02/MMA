import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import cv2
import numpy as np
import database.utils as db_utils
import compute_descriptor
import match
import utils 

# read all images from test data 
images = db_utils.read_images("matching-evaluation/test-images")


db_path = "database/db.txt"

accuracy = 0
for image in images:

    if (image[0] == ".DS_Store"):
        continue

    cont = image[1]
    match_list = match.sift_match(cont, db_path)

    # get the top prediction and compare with the truth label
    name = utils.extract_name(image[0])
    pred = utils.extract_name(match_list[0][0])

    if (name == pred):
        accuracy += 1
    print(name, pred, "accuracy =", accuracy / len(images))
    pass