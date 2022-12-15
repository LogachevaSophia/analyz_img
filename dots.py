# importing the module
import cv2
import main

# function to display the coordinates of
# of the points clicked on the image


def click_event(event, x, y, flags, params):
    global p, filename,hold, p_dop

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        #image = cv2.circle(image, (x, y), radius=0, color=(0, 0, 255), thickness=-1)

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        fl = True
        print(x, ' ', y)
        for i in range(len(p)):
            if (x <= p[i][0] + 7) and (x >=  p[i][0]-7 ) and (y >= p[i][1] -7) and ((y <= p[i][1] +7)):
                print("попал в точку")
                fl = False
                hold = True
                p_dop = (p[i][0], p[i][1])
                print("Координаты центра точки, в которую попала: ", p_dop)
                break
        if fl:
            cv2.circle(img, (x, y), radius=7, color=(0, 0, 255), thickness=-1)
            p.append((x,y))
        print(p)    
        if len(p) == 4:
            p = sorted(p , key=lambda k: [k[1]])
            dop1 = sorted([p[0],p[1]] , key=lambda k: [k[0]])
            dop2 = sorted([p[2],p[3]] , key=lambda k: [k[0]])
            p = []
            p.append(dop1[0])
            p.append(dop1[1])
            p.append(dop2[0])
            p.append(dop2[1])
            cv2.line(img, p[2],p[3], (0, 0, 255))
            cv2.line(img, p[1],p[3], (0, 0, 255))
            cv2.line(img, p[0],p[1], (0, 0, 255))
            cv2.line(img, p[0],p[2], (0, 0, 255))
            cv2.imshow('image', img)
            main.perspective(p, filename)
        elif len(p) == 2:
            
            cv2.imshow('image', img)
        elif len(p) == 3:
            
            cv2.imshow('image', img)
        else:
            cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONUP:
        print("Отжал")
        if hold:
            img_copy = img.copy();
            ind = p.index(p_dop);
            p[ind] = (x,y)
            cv2.circle(img_copy, (x, y), radius=7, color=(0, 0, 255), thickness=-1)
            cv2.imshow('image', img_copy)
        print(p)


# driver function
p = [];
p_dop = ();
hold = False;

filename = 'book1.jpg'
    # reading the image
img = cv2.imread(filename, 1)

    # displaying the image
cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
cv2.waitKey(0)

    # close the window
cv2.destroyAllWindows()
