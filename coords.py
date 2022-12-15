import cv2
import numpy as np

def click_event_coords(event, x, y, flags, params):
    global coords, imgsorc
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, ' ', y)
        #cv2.circle(imgsorc, (x, y), radius=7, color=(0, 0, 255), thickness=-1)
        coords = (x,y,1)
        calculateCoord()
        




coords = []
M = []

def calculateCoord():
    
    global M,imgdest
    print(M)
    print(coords)
    
    M_new = np.linalg.inv(M)
    coords_new = [[coords[0]], [coords[1]], [coords[2]]]
    coorddest = np.dot(M,coords_new)
    print(coorddest)
    print("***************",(coorddest[1][0]))
    print((int(coorddest[0][0]),int(coorddest[1][0])))
    cv2.circle(imgdest, (int(coorddest[0][0]/coorddest[2][0]),int(coorddest[1][0]/coorddest[2][0])), radius=7, color=(0, 0, 255), thickness=-1)
    cv2.imshow('imageeeeeeeeeeee', imgdest)
 

imgsorc = []
imgdest = []

def coordsOnImage(file_name, file_name_src, Mat):
    #1 - file_name dest, 
    #2 - file_name_src
    print(file_name_src)
    global img
    global coords, M, imgdest
    M = Mat
    filename = file_name
    # reading the image
    imgsorc = cv2.imread(file_name_src, 1)
    imgdest = cv2.imread(file_name, 1)

    # displaying the image
    cv2.imshow('image', imgsorc)
    cv2.setMouseCallback('image', click_event_coords)
    