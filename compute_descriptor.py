# compute the descriptor based on interest points from an image
# input: an image
# output: a list of corresponding descriptors

import cv2 

def sift_descriptor(image):
    sift = cv2.xfeatures2d.SIFT_create(nfeatures = 500)

    kp, des = sift.detectAndCompute(image, None)

    return kp, des  
    pass