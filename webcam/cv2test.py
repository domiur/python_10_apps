import cv2
import glob
import numpy as np

img13=[]
def rw_image(path=".*",resize_factor=1.,crop_factor=0.9,angle=0.,shift=(20,30),blur=0,thresh=0,edge=0):
    list=glob.glob(path)

    for file in list:
        img=cv2.imread(file,cv2.IMREAD_UNCHANGED)
        #UNCHANGED)
        h,w=img.shape[:2]

        #crop
        img0=img[int(h*(1-crop_factor)):int(h*crop_factor),
                 int(w*(1-crop_factor)):int(w*crop_factor)]

        #resize
        img1=cv2.resize(img0,( int(w*resize_factor),int(h*resize_factor) )) # or
        #img1=cv2.resize(img,None,fx=resize_factor,fy=resize_factor)

        #rotation
        center = (w/2, h/2)
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1)
        img2 = cv2.warpAffine(src=img1, M=rotate_matrix, dsize=(w, h))

        #translation
        translation_matrix = np.array([
	        [1, 0, shift[0]],
	        [0, 1, shift[1]]
	    ], dtype=np.float32)  
        img3 = cv2.warpAffine(src=img2, M=translation_matrix, dsize=(w, h))

        #draw 
            #line
        img4=cv2.line(img3,(0,0),(600,600),color=(255,255,0),thickness=3)
            #circle
        img5=cv2.circle(img4, center=(250,250), radius=100, color=(0, 0, 255), thickness=3, lineType=cv2.LINE_AA) 
            #filled circle: thickeness=-1
        img6=cv2.circle(img5, center=(250,250), radius=50, color=(0, 0, 255), thickness=-1, lineType=cv2.LINE_AA) 
            #rectangle 
        img7=cv2.rectangle(img6, pt1=(0,250), pt2=(250,0), color=(0, 255, 0), thickness=4, lineType=cv2.LINE_AA) 
            #ellipse 
        img8=cv2.ellipse(img7,center=(300,500),axes=(100,50),angle=45, startAngle=0,endAngle=180,
            color=(255, 0, 0), thickness=4, lineType=cv2.LINE_AA) 
           #filled ellipse 
        img9=cv2.ellipse(img8,center=(300,500),axes=(100,50),angle=-45, startAngle=0,endAngle=180,
            color=(255, 255, 0), thickness=-1, lineType=cv2.LINE_AA) 
          #text
        img10=cv2.putText(img9,"tra-ta-ta!",org=(100,500),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,
            color=(255, 255, 0), thickness=2, lineType=cv2.LINE_AA) 
        if blur==1:
            kernel = np.array([[0, 0, 0],
                                [0, 1, 0],
	                            [0, 0, 0]])
            img11 = cv2.filter2D(img10, ddepth=-1, kernel=kernel)
        elif blur==2:
            img11 = cv2.GaussianBlur(img10,ksize=(5,5),sigmaX=10,sigmaY=10)
        elif blur==3:
            img11 = cv2.medianBlur(img10,ksize=25)
        elif blur==4: #sharpen
            kernel = np.array([[0, -1, 0],
                                [-1, 5, -1],
	                            [0, -1, 0]])
            img11 = cv2.filter2D(img10, ddepth=-1, kernel=kernel)
        elif blur==5:
            img11 = cv2.bilateralFilter(img10,d=9,sigmaSpace=75,sigmaColor=75)
        else:
            img11=img10

        if thresh>0:
            th, img12 = cv2.threshold(img11, thresh, 255, cv2.THRESH_BINARY)
            print(th)

        global img13
        if edge==1:
            img13 = cv2.Canny(img12, threshold1=100, threshold2=200)
        elif edge==2:
            img_blur = cv2.GaussianBlur(img12,(3,3), sigmaX=10, sigmaY=10) 
            img13 = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
        else:
            img13=img12

        print(img13.shape)
        cv2.namedWindow("Window")
        cv2.setMouseCallback("Window", drawRectangle,param=[img13])
        global top_left_corner, bottom_right_corner

        top_left_corner=[]
        bottom_right_corner=[]

        while True:
            cv2.imshow("Window",img13)
            if cv2.waitKey(0)==ord('q'):
                break
        #cv2.imwrite('grayscale.jpg',img_grayscale)
    cv2.destroyAllWindows()

# function which will be called on mouse input
top_left_corner=[]
bottom_right_corner=[]

def drawRectangle(action, x, y, flags, *userdata):
    global top_left_corner, bottom_right_corner,img13
    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner.append((x,y))
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner.append((x,y))
        #q=img13
        q=np.array(userdata[0])[0]
        print(q.shape)
        for p1,p2 in zip(top_left_corner,bottom_right_corner):
            print(p1,p2)
            cv2.rectangle(q, p1, p2, (0,255,0),2, 8)
        #cv2.rectangle(q, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
        cv2.imshow("Window",q)



rw_image("*.jpg",resize_factor=.5,crop_factor=0.9,angle=-45.,shift=(50,500),blur=5,thresh=10,edge=0)