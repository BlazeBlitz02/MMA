# compute the descriptor based on interest points from an image
# input: an image
# output: a list of corresponding descriptors

import cv2 
import numpy as np

def sift_descriptor(image):
    # define and compute sift keypoints & descriptors
    sift = cv2.SIFT_create()
    kp, des = sift.detectAndCompute(image, None)

    # define the number of best descriptor
    n_desc = 500 

    # extract the response for selecting only the best keypoints
    indices = np.argsort(list(map(lambda x : x.response, kp)))[-n_desc:]


    # convert to np array
    kp = np.array(kp)[indices]
    des = np.array(des)[indices]

    # return result
    return kp, des  
    pass