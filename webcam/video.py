import cv2,time


video=cv2.VideoCapture(0)
first_frame=None

check=True
key=0
while video.isOpened() and check==True and key != ord('q'):
    check,frame=video.read()

    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey=cv2.GaussianBlur(grey,(21,21),0)
    if first_frame is None:
        first_frame=grey
        continue

    delta_frame=cv2.absdiff(first_frame,grey)
    thresh_frame=cv2.threshold(delta_frame,10,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=5)
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        if cv2.contourArea(cnt)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("",frame)
    cv2.imshow("qq",delta_frame)
    cv2.imshow("q1q",thresh_frame)

    key=cv2.waitKey(1)

cv2.destroyAllWindows()
video.release()