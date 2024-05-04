import cv2
import numpy as np

img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg')
width = 600
height = 500
dim = (width,height)
resized = cv2.resize(img,dim)

kernel = np.ones((5,5),dtype='uint8')

#erosion = cv2.erode(resized,kernel,iterations=1) # more no of iterations more erosion takes place
#dilation = cv2.dilate(resized,kernel,iterations=1)
#opening = cv2.morphologyEx(resized,cv2.MORPH_OPEN,kernel)
#closing = cv2.morphologyEx(resized,cv2.MORPH_CLOSE,kernel)
#gradient = cv2.morphologyEx(resized,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Original",resized)
#cv2.imshow("Erosion",erosion)
#cv2.imshow("Dilation",dilation)
#cv2.imshow("Opening",opening)
#cv2.imshow("Closing",closing)
#cv2.imshow("Gradient",gradient)
cv2.imshow("Tophat",tophat)
cv2.imshow("Blackhat",blackhat)


cv2.waitKey(0)
cv2.destroyAllWindows()