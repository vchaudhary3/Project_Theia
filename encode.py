"""
Created on Sat Oct 20 05:13:29 2018
face recognition
@author: Vedantika Chaudhary
"""

# import the necessary packages
from imutils import paths
import face_recognition
import pickle
import cv2
import os

PATH_TO_DATASET = "C:\\Users\\Siddhant\\Documents\\GitHub\\Project_Theia\\data_set"
DETECTION_METHOD = "hog" # or "cnn"
PATH_TO_USER = "C:\\Users\\Siddhant\\Documents\\GitHub\\Project_Theia\\Users"
WRITE_FILE = "collin.txt"

def generate_encodings():
    # grab the paths to the input images in our dataset
    #print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images(PATH_TO_DATASET))
     
    # initialize the list of known encodings and known names
    knownEncodings = []
    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
     
    	# load the input image and convert it from BGR (OpenCV ordering)
    	# to dlib ordering (RGB)
    	image = cv2.imread(imagePath)
    	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
       
    
    	# detect the (x, y)-coordinates of the bounding boxes
    	# corresponding to each face in the input image
    	boxes = face_recognition.face_locations(rgb, model=DETECTION_METHOD)
    
    	# compute the facial embedding for the face
    	encodings = face_recognition.face_encodings(rgb, boxes)
    
    	# loop over the encodings
    	for encoding in encodings:
    		# add each encoding + name to our set of known names and encodings
    		knownEncodings.append(encoding)
    
    data = {"encodings": knownEncodings}
    f = os.open(PATH_TO_USER + WRITE_FILE, "wb")
    f.write(pickle.dumps(data))
    f.close()