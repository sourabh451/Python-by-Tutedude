# pip install numpy
# pip install opencv-python
import cv2

#img = cv2.imread("D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg",0)
img = cv2.imread("D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/highway.jpg",1)

print("Dimensions of the image: ",img.shape)

#width = img.shape[1] # if width of img is unchanged
#height = 400
width = 400
height = img.shape[1]
dim = (width,height)
resized = cv2.resize(img,dim)

cv2.imshow("window",resized)

cv2.imwrite('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/car.jpg',img)

cv2.waitKey(0)

cv2.destroyAllWindows()