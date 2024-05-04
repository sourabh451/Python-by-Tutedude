import cv2

video = cv2.VideoCapture('D:/Tutedude/Python/18OPEN_CV/18.1CONTENT FILES/nature.mp4')

while video.isOpened():
    _,frame = video.read()
    frame = cv2.resize(frame,(800,720))

    cv2.imshow('Output',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()