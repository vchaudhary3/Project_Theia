# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 05:29:00 2018

@author: Vedantika Chaudhary
"""

# import the necessary packages
#from imutils.video import VideoStream
import face_recognition
#import argparse
#import imutils
import pickle
import time
import cv2
 
# construct the argument parser and parse the arguments

 
PATH_TO_ENCODING = "/Users/zak/Desktop/Project_Theia/users/collin.txt"
DETECTION_METHOD = "hog" # or "cnn"
MAX = 10
ACCURACY = 8
# load the known faces and embeddings
def recognize():
    data = pickle.loads(open(PATH_TO_ENCODING, "rb").read())
     
    # initialize the video stream and pointer to output video file, then
    # allow the camera sensor to warm up
    
    camera = cv2.VideoCapture(0)
    time.sleep(2)
    numCorrect = 0
    checks = 0
    # loop over frames from the video file stream
    while checks <= MAX:
    	# grab the frame from the threaded video stream
    	valid, frame = camera.read()
    	if not valid:
            print("Unable to connect to camera \n")
            break
        
    	# convert the input frame from BGR to RGB then resize it to have
    	# a width of 750px (to speedup processing)
    	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    	height, width, layers =  frame.shape
    	rgb = cv2.resize(frame, (750, int(((750*height)/width)) ))
    	r = frame.shape[1] / float(rgb.shape[1])
        
    	# detect the (x, y)-coordinates of the bounding boxes
    	# corresponding to each face in the input frame, then compute
    	# the facial embeddings for each face
    	boxes = face_recognition.face_locations(rgb,
    		model=DETECTION_METHOD)
    	encoding = face_recognition.face_encodings(rgb, boxes)
    	
        # loop over the facial embeddings
        # attempt to match each face in the input image to our known
        # encodings
    	match = face_recognition.compare_faces(data["encodings"],
    			encoding[0])
    	checks = checks + 1
    		# check to see if we have found a match
    	if match[0]:
            numCorrect = numCorrect + 1
    return (numCorrect >= ACCURACY)
        
print(recognize())
