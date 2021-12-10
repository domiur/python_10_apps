import numpy as np
import cv2
#from skimage import data, filters


video=cv2.VideoCapture(0)

check=True
key=0
num=25
frames=[]
while video.isOpened() and check==True and key != ord('q'):
    check,frame=video.read()

    if len(frames)<30:
        frames.append(frame)
    else:
        medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
        cv2.imshow("",medianFrame)
        frames.pop(0)
    key=cv2.waitKey(1)

cv2.destroyAllWindows()
video.release()

