# this file contains only helper methods
import numpy as np

# input a string
# output: name of the landmark that string contains
def extract_name(s):
    names = np.array(s.split("_"))
    return names[-1:][0].split(".")[0]
    pass