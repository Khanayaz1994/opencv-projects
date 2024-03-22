import cv2  
import numpy as np
import matplotlib.pyplot as plt
import math


if __name__ == "__main__":
    print("Hello OpenCV!!!")    
    
    pCameraHandle = cv2.VideoCapture(0)
    
    while True:
        
        errCode, frame = pCameraHandle.read()
        #error check
        gray         = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        histSize     = [256]
        histRange    = [0, 255]
        
        histogram    = cv2.calcHist(gray, [0], None, histSize, histRange )
        minVal, maxVal, MinLoc, MaxLoc = cv2.minMaxLoc(histogram)        
        
        print("minVal, maxVal, MinLoc, MaxLoc ", minVal, maxVal, MinLoc, MaxLoc)

        distRange = math.sqrt((MaxLoc[0]-MinLoc[0])*(MaxLoc[0]-MinLoc[0]) + 
                              (MaxLoc[1]-MinLoc[1])*(MaxLoc[1]-MinLoc[1]))

        print("distRange : ", distRange)
        if distRange < 50:
            print("Camera Tempered")
            cv2.putText(frame, "Camera Tempered", (30,30), 1, 1, (0, 0, 255), 2)
            

        plt.cla()
        plt.plot(histogram)  
        plt.show(block=False)
        plt.pause(0.001)
        
        cv2.imshow('input', frame)
        cv2.imshow('gray', gray)
        cv2.waitKey(30)
      
else:
    print("Camera Tempering file has been imported")
    