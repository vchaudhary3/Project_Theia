"""
Created on Sun Oct 21 02:26:02 2018

@author: Vedantika Chaudhary
"""
from PyQt5.QtWidgets import QApplication
import faceRecognition
import faceDetection
from pathlib import Path
import login
import encode
import turnoff
from GUI import App
import os
import time
import sys

WRITE_FILE = "/Users/zak/Desktop/Project_Theia/users/collin.txt" #has to be changed
PATH_TO_USERINFO ="/Users/zak/Desktop/Project_Theia/login.txt" # please fill

if __name__ == '__main__':
    my_file = Path(WRITE_FILE)
    print(my_file.is_file())
    if my_file.is_file():
        if(faceRecognition.recognize()):
            faceDetection.detect_face()
        else:
            app = QApplication([])
            ex = App(imgpath="/Library/User Pictures/Nature/Leaf.tif")
            app.exec_()
            a = ex.auth() 
            if(a == 1):
                faceDetection.detect_face()
            else:
                os.remove(WRITE_FILE)
                os.remove(PATH_TO_USERINFO)
                import subprocess
                subprocess.call('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend', shell=True)
    else:
        login.get_dataSet() 
        encode.generate_encodings()
        app = QApplication([])
        ex = App(imgpath="/Library/User Pictures/Nature/Leaf.tif")
        ex.register()
        app.exec_()


        
        
                
                
            
            
      
