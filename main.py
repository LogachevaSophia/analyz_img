import cv2
import numpy as np

img = cv2.imread("road.jpg")

width, height = 250, 250

# card
#pts1 = np.float32([[887,365], [1141,277], [1129,695], [1407,575]])

# road
pts1 = np.float32([[11,540], [395,483], [46,760], [502,669]])

# book
#pts1 = np.float32([[201, 161], [336, 233], [46, 300], [201, 425]])

pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

output = cv2.warpPerspective(img, matrix, (width, height))


for i in range(4):
    cv2.circle(img, (pts1[i][0], pts1[i][1]), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original img", img)

cv2.imshow("Perspecive", output)

cv2.waitKey(0)
