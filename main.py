#import cv2
#import numpy as np

#img = cv2.imread("book1.jpg")

#width, height = 250, 450

# card
#pts1 = np.float32([[887,365], [1141,277], [1129,695], [1407,575]])

# road
#pts1 = np.float32([[11,540], [395,483], [46,760], [502,669]])

# book
#pts1 = np.float32([[201, 161], [336, 233], [46, 300], [201, 425]])

#pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

#matrix = cv2.getPerspectiveTransform(pts1, pts2)

#print(matrix)

#output = cv2.warpPerspective(img, matrix, (width, height))


#cv2.circle(img, (50,550), 5, (0, 255, 0), cv2.FILLED)

#for i in range(4):
 #   cv2.circle(img, (pts1[i][0], pts1[i][1]), 5, (0, 0, 255), cv2.FILLED)

#cv2.imshow("Original img", img)

#cv2.imshow("Perspecive", output)

#cv2.waitKey(0)
import math
import cv2
import scipy.spatial.distance
import numpy as np

img = cv2.imread('cards.jpg')
(rows,cols,_) = img.shape

#image center
u0 = (cols)/2.0
v0 = (rows)/2.0

#detected corners on the original image/обнаруженные углы на исходном изображении
p = []
p.append((887,365))
p.append((1141,277))
p.append((1129,695))
p.append((1407,575))

#widths and heights of the projected image/ ширина и высота проецируемого изображения
w1 = scipy.spatial.distance.euclidean(p[0],p[1])
w2 = scipy.spatial.distance.euclidean(p[2],p[3])

h1 = scipy.spatial.distance.euclidean(p[0],p[2])
h2 = scipy.spatial.distance.euclidean(p[1],p[3])

w = max(w1,w2)
h = max(h1,h2)

#visible aspect ratio/ видимые пропорции
ar_vis = float(w)/float(h)

#make numpy arrays and append 1 for linear algebra/создать массивы numpy и добавить 1 для линейной алгебры

m1 = np.array((p[0][0],p[0][1],1)).astype('float32')
m2 = np.array((p[1][0],p[1][1],1)).astype('float32')
m3 = np.array((p[2][0],p[2][1],1)).astype('float32')
m4 = np.array((p[3][0],p[3][1],1)).astype('float32')

#calculate the focal disrance/ рассчитать фокусное отклонение

k2 = np.dot(np.cross(m1,m4),m3) / np.dot(np.cross(m2,m4),m3)
k3 = np.dot(np.cross(m1,m4),m2) / np.dot(np.cross(m3,m4),m2)

n2 = k2 * m2 - m1
n3 = k3 * m3 - m1

n21 = n2[0]
n22 = n2[1]
n23 = n2[2]

n31 = n3[0]
n32 = n3[1]
n33 = n3[2]

f = math.sqrt(np.abs( (1.0/(n23*n33)) * ((n21*n31 - (n21*n33 + n23*n31)*u0 + n23*n33*u0*u0) + (n22*n32 - (n22*n33+n23*n32)*v0 + n23*n33*v0*v0))))

A = np.array([[f,0,u0],[0,f,v0],[0,0,1]]).astype('float32')

At = np.transpose(A)
Ati = np.linalg.inv(At)
Ai = np.linalg.inv(A)

#calculate the real aspect ratio/ рассчитать реальное соотношение сторон

ar_real = math.sqrt(np.dot(np.dot(np.dot(n2,Ati),Ai),n2)/np.dot(np.dot(np.dot(n3,Ati),Ai),n3))

if ar_real < ar_vis:
    W = int(w)
    H = int(W / ar_real)
else:
    H = int(h)
    W = int(ar_real * H)

pts1 = np.array(p).astype('float32')
pts2 = np.float32([[0,0],[W,0],[0,H],[W,H]])

#project the image with the new w/h
M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(W,H))

cv2.imshow('img',img)
cv2.imshow('dst',dst)


cv2.waitKey(0)
