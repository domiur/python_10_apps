import cv2
import glob
import numpy as np
import math

mode=""
infile="news.jpg"

top_left_corner=[]
bottom_right_corner=[]

def show_image():
    cv2.imshow("Window",image)

def edit_image(): 
    global mode
    while True:
        show_image()
        key=cv2.waitKey(0)
        if key==ord('q'):
            break
        elif key==ord('r'):
            mode="rect"
        elif key==ord('c'):
            mode="circle"
        elif key==ord('l'):
            mode="line"
        elif key==ord('p'):
            mode="polyline"
        elif key==ord('w'):
            arr=infile.split(".")
            outfile=".".join(arr[0:len(arr)-1])+".out."+arr[-1]
            print(outfile,len(arr))
            cv2.imwrite(outfile,image)
            break
        else:
            mode=""
        
    cv2.destroyAllWindows()


def mouseEventProcessing(action, x, y, flags, *userdata):
    global top_left_corner, bottom_right_corner
    if mode=="rect":
        if action == cv2.EVENT_LBUTTONDOWN:
            top_left_corner=[(x,y)]
        elif action == cv2.EVENT_LBUTTONUP:
            bottom_right_corner=[(x,y)]
            cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
            show_image()

    elif mode=="line":
        if action == cv2.EVENT_LBUTTONDOWN:
            top_left_corner=[(x,y)]
        elif action == cv2.EVENT_LBUTTONUP:
            bottom_right_corner=[(x,y)]
            cv2.line(image,top_left_corner[0],bottom_right_corner[0],color=(255,255,0),thickness=3)
            show_image()
   
    elif mode=="polyline":
        if action == cv2.EVENT_LBUTTONDOWN:
            top_left_corner=[(x,y)]
        elif action == cv2.EVENT_LBUTTONUP:
            bottom_right_corner=[(x,y)]
            cv2.line(image,top_left_corner[0],bottom_right_corner[0],color=(255,255,0),thickness=3)
            top_left_corner=[(x,y)]
            show_image()

    elif mode=="circle":
        if action == cv2.EVENT_LBUTTONDOWN:
            top_left_corner=[(x,y)]
        elif action == cv2.EVENT_LBUTTONUP:
            bottom_right_corner=[(x,y)]
            r=math.sqrt( (x-top_left_corner[0][0])**2 + (y-top_left_corner[0][1])**2 )
            cv2.circle(image, center=( int((top_left_corner[0][0]+x)/2), int((top_left_corner[0][1]+y)/2) ),  radius=int(r/2), color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA) 
            show_image()

image=cv2.imread(infile,cv2.IMREAD_UNCHANGED)
height,wifth=image.shape[:2]
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", mouseEventProcessing,param=[image])

edit_image()