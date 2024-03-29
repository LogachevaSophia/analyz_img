
import math
import cv2
import scipy.spatial.distance
import numpy as np



def perspective(_p, file_name):
    
    #сортировка точек
    dop1 = sorted([_p[0], _p[1]], key=lambda k: [k[0]])
    dop2 = sorted([_p[2], _p[3]], key=lambda k: [k[0]])
    p = []
    p.append(dop1[0])
    p.append(dop1[1])
    p.append(dop2[0])
    p.append(dop2[1])
    img = cv2.imread(file_name)
    (rows, cols, _) = img.shape

# image center
    u0 = (cols)/2.0
    v0 = (rows)/2.0

# detected corners on the original image/обнаруженные углы на исходном изображении
    #p = []
# p.append((201, 161))
# p.append((336, 233))
# p.append((46, 300))
# p.append((201, 425))

# widths and heights of the projected image/ ширина и высота проецируемого изображения
    w1 = scipy.spatial.distance.euclidean(p[0], p[1])
    w2 = scipy.spatial.distance.euclidean(p[2], p[3])

    h1 = scipy.spatial.distance.euclidean(p[0], p[2])
    h2 = scipy.spatial.distance.euclidean(p[1], p[3])

    w = max(w1, w2)
    h = max(h1, h2)

# visible aspect ratio/ видимые пропорции
    ar_vis = float(w)/float(h)

# make numpy arrays and append 1 for linear algebra/создать массивы numpy и добавить 1 для линейной алгебры

    m1 = np.array((p[0][0], p[0][1], 1)).astype('float32')
    m2 = np.array((p[1][0], p[1][1], 1)).astype('float32')
    m3 = np.array((p[2][0], p[2][1], 1)).astype('float32')
    m4 = np.array((p[3][0], p[3][1], 1)).astype('float32')

# calculate the focal disrance/ рассчитать фокусное отклонение

    k2 = np.dot(np.cross(m1, m4), m3) / np.dot(np.cross(m2, m4), m3)
    k3 = np.dot(np.cross(m1, m4), m2) / np.dot(np.cross(m3, m4), m2)

    n2 = k2 * m2 - m1
    n3 = k3 * m3 - m1

    n21 = n2[0]
    n22 = n2[1]
    n23 = n2[2]

    n31 = n3[0]
    n32 = n3[1]
    n33 = n3[2]

    f = math.sqrt(np.abs((1.0/(n23*n33)) * ((n21*n31 - (n21*n33 + n23*n31) *
                  u0 + n23*n33*u0*u0) + (n22*n32 - (n22*n33+n23*n32)*v0 + n23*n33*v0*v0))))

    A = np.array([[f, 0, u0], [0, f, v0], [0, 0, 1]]).astype('float32')

    At = np.transpose(A)
    Ati = np.linalg.inv(At)
    Ai = np.linalg.inv(A)

# calculate the real aspect ratio/ рассчитать реальное соотношение сторон

    ar_real = math.sqrt(np.dot(np.dot(np.dot(n2, Ati), Ai),
                        n2)/np.dot(np.dot(np.dot(n3, Ati), Ai), n3))

    if ar_real < ar_vis:
        W = int(w)
        H = int(W / ar_real)
    else:
        H = int(h)
        W = int(ar_real * H)

    print(W)
    print(H)

    pts1 = np.array(p).astype('float32')
    pts2 = np.float32([[0, 0], [W, 0], [0, H], [W, H]])

# project the image with the new w/h
    #M = cv2.getPerspectiveTransform(pts1,pts2)

    im_src = cv2.imread(file_name)
    size = (W, H)

    # Destination coordinates locate0 in the center of the image
    pts_dst = np.float32(
        [
            [im_src.shape[1]/2 - size[0]/2, im_src.shape[0]/2 - size[1]/2],
            [im_src.shape[1]/2 + size[0]/2, im_src.shape[0]/2 - size[1]/2],

            [im_src.shape[1]/2 - size[0]/2, im_src.shape[0]/2 + size[1]/2],
            [im_src.shape[1]/2 + size[0]/2, im_src.shape[0]/2 + size[1]/2]
        ]
    )

    M = cv2.getPerspectiveTransform(pts1, pts_dst)
    return {'M':M, 'W':W, 'H':H}
    #dst = cv2.warpPerspective(img,M,(W,H))
    # dst = cv2.warpPerspective(img, M, (im_src.shape[1], im_src.shape[0]))

    # cv2.imwrite('dst.jpg', dst)
    # coords.coordsOnImage('dst.jpg', file_name, M)
    # cv2.waitKey(0)
