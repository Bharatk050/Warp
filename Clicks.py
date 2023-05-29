import cv2
import numpy as np

circle = np.zeros((4,2), np.int)
counters = 0
scale = 0.5

def Points(event, x, y, flags, params):
    global counters
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, y)
        circle[counters] = x, y
        counters = counters + 1
        # print(circle) 

img = cv2.imread("<File_path>")
img = cv2.resize(img, (0,0), fx= scale, fy= scale)
while True:
    
    if counters == 4:
        width, height = 350, 450
        pts1 = np.float32([circle[0], circle[1], circle[2], circle[3]]) # *scale
        pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
        martix = cv2.getPerspectiveTransform(pts1, pts2)
        output = cv2.warpPerspective(img, martix, (width, height))
        cv2.imshow('Warped', output)

    cv2.imshow('Original', img)
    cv2.setMouseCallback('Original', Points)
    if cv2.waitKey(1) == ord('q'):
        break

