# CHANNEL --> 0 TO 255

import cv2
import numpy as np

#img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg')
img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg',0)

#threshold_value = 200
threshold_value = 100

_,binary_threshold = cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow('Original',img)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()