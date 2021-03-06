from dis import dis
from threading import current_thread
import database.utils as db_utils
from compute_descriptor import *
import cv2 
import numpy as np

global_descriptors = None
current_database_path = ""

# input: an image frame, database path
# output: a list from [image, distance]
def sift_match(image, database_path, num_best_match = 40):
    global global_descriptors
    global current_database_path

    if (global_descriptors is None or current_database_path != database_path):
        current_database_path = database_path
        global_descriptors = db_utils.read_database(database_path)


    kp1, descriptors_1 = sift_descriptor(image)


    res = []
    for item in global_descriptors:

        name = item[0]
        descriptors_2 = item[1]

        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

        matches = bf.match(descriptors_1,descriptors_2)

        matches = sorted(matches, key = lambda x:x.distance)    

        # compute the best distance within the top num_best_match matches
        best_distance = list(map(lambda x : x.distance, matches[:num_best_match]))
        sum_ = np.sum(best_distance)   

        res.append([name, sum_])

    # smaller the distance, the better
    res.sort(key = lambda x : x[1])
    return res
    pass
