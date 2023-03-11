import math
import cv2
import scipy.spatial.distance
import numpy as np


def modify(M, fileName, W, H, destFile):
    img = cv2.imread(fileName)
    
    im_src = cv2.imread(fileName)
    dst = cv2.warpPerspective(img, M, (W, H))
    dst = cv2.warpPerspective(img, M, (im_src.shape[1], im_src.shape[0]))
    cv2.imwrite(destFile, dst)
    

