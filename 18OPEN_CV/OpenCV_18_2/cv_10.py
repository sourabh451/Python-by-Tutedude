import cv2

img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg')

resize = cv2.resize(img,(520,520))

kernal = 3

blur = cv2.medianBlur(resize,kernal)

cv2.imshow('Input',resize)
cv2.imshow('Output',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()