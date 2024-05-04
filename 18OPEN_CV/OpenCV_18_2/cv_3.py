import cv2

img = cv2.imread('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg')
width = 600
height = 850
dim = (width,height)

resized = cv2.resize(img,dim)
print('Size in bytes:',img.size)
cv2.imshow('Original',resized)

#flip = cv2.flip(resized,1)
#cv2.imshow('Horizontal',flip)

#flip_1 = cv2.flip(resized,0)
#cv2.imshow('Vertical',flip_1)

flip_2 = cv2.flip(resized,-1)
cv2.imshow('Horizontal & Vertical',flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()