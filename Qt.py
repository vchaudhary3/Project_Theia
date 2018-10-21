#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import pyqtSlot, Qt
import time 
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Project Theia'
        self.left = 10
        self.top = 10
        self.width = 1920
        self.height = 1080
        self.initUI()
    
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
       
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(580, 460)
        self.textbox.resize(280,20)
 
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
        self.showFullScreen()

  
        
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    def resetCursor(self):
        cursor = QCursor()
        pos = cursor.pos()
        y = pos.y()
         
        while (y<10):
             cursor.setPos(1920,1080)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.setOverrideCursor(QCursor(Qt.BlankCursor))
    ex.resetCursor()
    sys.exit(app.exec_())
    


