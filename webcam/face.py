import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread("news.jpg")
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(img_grey,scaleFactor=1.06,minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=3)
cv2.imshow("",img)

cv2.waitKey(0)