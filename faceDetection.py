# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 03:58:17 2018

@author: Siddhant
"""
import time
import numpy as np
import cv2 as cv


'''Both are good but lbpcascades & full_face works better'''
#PATH_TO_HAARCASCADES = 'C:\\Users\\Siddhant\\Python\\Project Vision\\opencv-master\\data\\haarcascades\\'
#FRONTALFACE_DEFAULT = 'haarcascade_frontalface_default.xml'
PATH_TO_LBPCASCADES = '/Users/zak/Desktop/Project_Theia/lbpcascade_frontalface_improved.xml'
#FULL_FACE = 'lbpcascade_frontalface_improved.xml'
WAIT_TIME = 3

def detect_face():
    #variable that stores number of faces detected
    numfaces = -1
    face_cascade = cv.CascadeClassifier(PATH_TO_LBPCASCADES)
    camera = cv.VideoCapture(0);
    while True:
        (valid, frame) = camera.read()
        if not valid:
            print("Unable to connect to camera. faceDetection.py")
            break
        frame_g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #img = cv.imread('face.jpg')
        #frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(frame_g, 1.3, 5)
        numFaces = len(faces)
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = frame_g[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        
        cv.imshow('Window',frame)
        if(numFaces != 1):
            t_0 = time.time()
            if timer(WAIT_TIME, t_0, face_cascade, camera):
                print("TIME TO LONG OUT")
                break
            
        key = cv.waitKey(1) & 0xFF
        if(key == ord("q")):
            break
    
        cv.waitKey(1)
            
    cv.destroyAllWindows()
    camera.release()
    
def timer(time_len, t_0, face_cascade, camera):
    t = 0
    while t < time_len:
        (valid, frame) = camera.read()
        if not valid:
            print("Unable to connect to camera")
            break
        frame_g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame_g, 1.3, 5)
        numFaces = len(faces)
        t = time.time() - t_0;
        cv.imshow('Window', frame)
        cv.waitKey(1)
        if(numFaces == 1):
            return 0
    return 1
    
def face_recognition(face):
    print("FACE RECOGNITION HAPPENS")     
    
    
def get_dataset():
    print("GET DATA SET")

detect_face()
