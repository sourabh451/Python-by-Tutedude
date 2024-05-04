# Canny Edge Detection
#1 Noise reduction
#2 Intensity of the gradient of the image
#3 Non-maximum suppression
#4 Thresholding

import cv2
import numpy as np

#img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/bird.jpg',0)
img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/bird.jpg')
resize = cv2.resize(img,(520,520))
min_thresh = 100
max_thresh = 200
edges = cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow('Original',resize)
cv2.imshow('Edges',edges)

cv2.waitKey()
cv2.destroyAllWindows()