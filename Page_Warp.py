import cv2
import numpy as np
from numpy.core.defchararray import partition

img = cv2.imread("C:\\Users\\computer\\Desktop\\Space\\15\\OpenCV_PRO\\Warp\Photos\\1.jpg")
img = cv2.resize(img, (0,0), fx= 0.5, fy= 0.5)

width, height = 350, 450
pts1 = np.float32([[156, 304], [754, 295], [78, 1181], [825, 1183]]) * 0.5
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
martix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, martix, (width, height))
# print(pts1)


cv2.imshow('Original', img)
cv2.imshow('Warped', output)
cv2.waitKey(0)

