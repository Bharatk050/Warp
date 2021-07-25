import cv2
import numpy as np

img = cv2.imread("C:\\Users\\computer\\Desktop\\Space\\15\\OpenCV_PRO\\Warp\\Photos\\Cards3.jpg")
img = cv2.resize(img, (0,0), fx= 0.5, fy= 0.5)

width, height = 350, 450
pts1 = np.float32([[475, 138], [783, 358], [126, 536], [440, 788]]) * 0.5
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
martix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, martix, (width, height))
# print(pts1)


cv2.imshow('Original', img)
cv2.imshow('Warped', output)
cv2.waitKey(0)

