"""
Created on Sun Oct 21 02:26:02 2018

@author: Vedantika Chaudhary
"""
from pathlib import Path
import faceRecognition
import faceDetection
import os.path
import login
import encode
import turnoff
import GUI

WRITE_FILE = "collin.txt" #has to be changed
PATH_TO_USERINFO ="" # please fill

def main():
    if(Path(WRITE_FILE).isfile() and Path(PATH_TO_USERINFO).isfile()):
        if(faceRecognition.recognize()):
            faceDetection.detect_face()
        else:
            if(GUI.prompt_password()):
                faceDetection.detect_face()
            else:
                os.unlink(WRITE_FILE)
                os.unlink(PATH_TO_USERINFO)
                turnoff.turn_off();
    else:
        GUI.save_Txt()
        login.get_dataSet();
        encode.generate_encodings()
        faceDetection.detect_face()
        
        
                
                
            
            
      