#!/usr/bin/env python
import sys
import os
import datetime
import time
import re
import time 


if sys.platform.startswith('linux'):
	import os
	os.system("xset dpms force off")

elif sys.platform.startswith('win'):
	import win32gui
	import win32con
	from os import getpid, system
	from threading import Timer
	
	def force_exit():
		pid = getpid()
		system('taskkill /pid %s /f' % pid)
	
	t = Timer(1, force_exit)
	t.start()
	SC_MONITORPOWER = 0xF170
	win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
	t.cancel()

elif sys.platform.startswith('darwin'):
	import subprocess
	sleeptime = datetime.datetime.now() + datetime.timedelta(seconds=5)
	sleeptime = sleeptime.strftime('"%m/%d/%y %H:%M:%S"')
	os.system("sudo pmset schedule wake " + sleeptime)
	
	while(1):
                subprocess.call('echo \'tell application "Finder" to sleep\' | osascript', shell=True)
                ans = input("Enter a q or else: ")
                if(ans == "q"):
                        sys.exit() 
                





                
        





        
	
	
	


	
	

	
	

        

	


	


	


	

	
