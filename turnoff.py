#!/usr/bin/env python
import sys
import os

if sys.platform.startswith('linux'):
        import os
        os.system("xset dpms force off")

elif sys.platform.startswith('win'):
        import subprocess
        subprocess.call("turnoff.exe")

        
elif sys.platform.startswith('darwin'):
        import subprocess
        subprocess.call('echo \'tell application "Finder" to sleep\' | osascript', shell=True)



        

                





                
        





        
        
        
        


        
        

        
        

        

        


        


        


        

        
