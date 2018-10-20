# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 03:58:17 2018

@author: Siddhant
"""

import numpy as np
import cv2 as cv

PATH_TO_HAARCASCADES = 'C:\\Users\\Siddhant\\Python\\Project Vision\\opencv-master\\data\\haarcascades\\'
FRONTALFACE_DEFAULT = 'haarcascade_frontalface_default.xml'
'''Both are good but lbpcascades works better'''
PATH_TO_LBPCASCADES = 'C:\\Users\\Siddhant\\Python\\Project Vision\\opencv-master\\data\\lbpcascades\\'
FULL_FACE = 'lbpcascade_frontalface_improved.xml'

def detect_face():
    #variable that stores number of faces detected
    numfaces = -1
    face_cascade = cv.CascadeClassifier(PATH_TO_LBPCASCADES + FULL_FACE)
    camera = cv.VideoCapture(0);
    while True:
        (valid, frame) = camera.read()
        if not valid:
            """RETURN ERROR CODE"""
            print("Unable to connect to camera")
        frame_g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #img = cv.imread('face.jpg')
        #frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(frame_g, 1.3, 5)
        numFaces = len(faces)
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = frame_g[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        
        key = cv.waitKey(1) & 0xFF
        if(key == ord("q")):
            break
    
        cv.waitKey(1)
   cv.destroyAllWindows()
        

main()    


