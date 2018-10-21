# when we login 
# import the necessary packages
#from imutils.video import VideoStream
#import imutils
import time
import cv2
import os

"""PATH TO CASCADE & OUTPUT OF DATASET"""

PATH_TO_DATASET = "/Users/zak/Desktop/Project_Theia/data_set"
RATE = 2 #frame rate
 
# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far

def get_dataSet():
    
    camera = cv2.VideoCapture(0)
    numPics = 0
    counter = 0
    print("Please wait for the computer to recognize your face")
    # loop over the frames from the video stream
    while numPics <= 25:
        (valid, frame) = camera.read()
        if not valid:
            print("Unable to connect to camera. faceDetection.py")
            break
        copy = frame.copy()
        
        counter = counter + 1
        counter = counter % RATE
            
        if (counter == 0 and numPics <= 20):
            p = os.path.sep.join([PATH_TO_DATASET, "{}.png".format(str(numPics).zfill(5))])
            cv2.imwrite(p, copy)
            numPics = numPics + 1
            
        key = cv2.waitKey(1) & 0xFF
        if(key == ord("q")):
            break

        if(numPics <= 20):
            cv2.putText(frame, "Setting up your face", (500,700), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "SUCCESS", (600,700), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("frame",  frame)

        if(numPics > 20):
            numPics = numPics + 0.25
        cv2.waitKey(1)
    

    cv2.destroyAllWindows()
    camera.release()

if __name__ == '__main__':
    get_dataSet()
