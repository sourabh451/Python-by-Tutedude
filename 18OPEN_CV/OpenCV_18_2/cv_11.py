import cv2

img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/bird.jpg')

resize = cv2.resize(img,(520,520))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(resize,d,sigmacolor,sigmaspace)

cv2.imshow('Input',resize)
cv2.imshow('Output',b)

cv2.waitKey()
cv2.destroyAllWindows()