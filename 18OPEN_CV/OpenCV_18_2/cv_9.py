import cv2

img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg')

resize = cv2.resize(img,(640,640))

ksize = (7,7)
sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow('Input',resize)
cv2.imshow('Output',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()