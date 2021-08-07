import cv2
import time
import random

# initialize cv2

def takesanpshot():
    videocaptureobject=cv2.VideoCapture(0)
    result= True
    while(result):
        # read the frames while the camera is on
        ret,frame= videocaptureobject.read()
        # cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture.jpg",frame)
        result=False

    #release the camera
    videocaptureobject. release()  

    #close all the windows that might be opened while this process
    cv2.destroyAllWindows()

takesanpshot()


    