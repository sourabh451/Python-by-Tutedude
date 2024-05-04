# pip install numpy
# pip install opencv-python
import cv2

#img = cv2.imread("D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg",0)
#img = cv2.imread("D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg",0)
img = cv2.imread("D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg",1)
cv2.imshow("window",img)

#cv2.waitKey(0)
cv2.waitKey(1000)

cv2.destroyAllWindows()