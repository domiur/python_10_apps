import cv2
import glob

list=glob.glob("*.jpg")
print(list)

for file in list:
    img=cv2.imread(file,1)
    print(img.shape)

    w=int(img.shape[1]*2)
    img1=cv2.resize(img,(int(img.shape[1]/img.shape[0]*w),w))
    cv2.imshow("",img1)
    cv2.waitKey(0)
cv2.destroyAllWindows()