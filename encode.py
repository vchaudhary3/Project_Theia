"""
Created on Sat Oct 20 05:13:29 2018
face recognition
@author: Vedantika Chaudhary
"""

# import the necessary packages
#from imutils import paths
from PIL import Image
import face_recognition
#from dlib import face_recognition_model_v1 as face_recognition
import pickle
import cv2
import os

PATH_TO_DATASET = "/Users/zak/Desktop/Project_Theia/data_set"
DETECTION_METHOD = "hog" # or "cnn"
PATH_TO_USER = "/Users/zak/Desktop/Project_Theia/users/collin.txt"
#WRITE_FILE = "collin.txt"

def generate_encodings():
    # grab the paths to the input images in our dataset
    #print("[INFO] quantifying faces...")
    imagePaths = []
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(PATH_TO_DATASET):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imagePaths.append(os.path.join(PATH_TO_DATASET,f))
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
    file = open(PATH_TO_USER, "wb")
    file.write(pickle.dumps(data))
    file.close()

generate_encodings()
