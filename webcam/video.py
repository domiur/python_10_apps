import cv2,time


video=cv2.VideoCapture(0)

check=True
key=0
while video.isOpened() and check==True and key != ord('q'):
    check,frame=video.read()

    cv2.imshow("",frame)

    key=cv2.waitKey(1)

cv2.destroyAllWindows()
video.release()