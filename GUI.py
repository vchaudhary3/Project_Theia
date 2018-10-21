#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QCursor, QBrush, QImage, QPainter, QPixmap, QWindow
from PyQt5.QtCore import pyqtSlot, Qt, QRect
#from passlib.apps import custom_app_context as pwd_context



def mask_image(imgdata, imgtype='tiff', size=96):
    # Load image and convert to 32-bit ARGB (adds an alpha channel):
    image = QImage.fromData(imgdata, imgtype)
    image.convertToFormat(QImage.Format_ARGB32)

    # Crop image to a square:
    imgsize = min(image.width(), image.height())
    rect = QRect(
        (image.width() - imgsize) / 2,
        (image.height() - imgsize) / 2,
        imgsize,
        imgsize,
    )
    image = image.copy(rect)

    # Create the output image with the same dimensions and an alpha channel
    # and make it completely transparent:
    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)

    # Create a texture brush and paint a circle with the original image onto
    # the output image:
    brush = QBrush(image)        # Create texture brush
    painter = QPainter(out_img)  # Paint the output image
    painter.setBrush(brush)      # Use the image texture brush
    painter.setPen(Qt.NoPen)     # Don't draw an outline
    painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
    painter.drawEllipse(0, 0, imgsize, imgsize)  # Actually draw the circle
    painter.end()                # We are done (segfault if you forget this)

    # Convert the image to a pixmap and rescale it.  Take pixel ratio into
    # account to get a sharp image on retina displays:
    pr = QWindow().devicePixelRatio()
    pm = QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    size *= pr
    pm = pm.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    return pm
 
class App(QWidget):
 
    def __init__(self, imgpath):
        super().__init__()
        self.title = 'Project Theia'
        self.left = 10
        self.top = 10
        self.width = 1920
        self.height = 1080
        self.initUI()
        self.setMouseTracking(True)
        self.flag = 0
        self.bool = True
        self.username = ""
        self.password = ""
        self.password1 = "" 

        imgdata = open(imgpath, 'rb').read()
        pixmap = mask_image(imgdata)
        ilabel = QLabel()
        ilabel.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(ilabel, 0, Qt.AlignCenter)
        self.setLayout(layout)

 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
       
        # Create 2 textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(580, 520)
        self.textbox.resize(280,20)
        self.textbox.setPlaceholderText("Enter Username")

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(580, 560)
        self.textbox1.resize(280,20)
        self.textbox1.setPlaceholderText("Enter Password")

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(580, 600)
        self.textbox2.resize(280,20)
        self.textbox2.setPlaceholderText("Confirm Password")
        self.textbox2.hide() 
        
        # Create a button in the window
        self.button = QPushButton('Submit', self)
        self.button.move(665,640)
        self.button.resize(100, 20) 
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
        self.showFullScreen()

         
    @pyqtSlot()
    def on_click(self):
        self.username = self.textbox.text()
        self.password = self.textbox1.text()

        if (self.flag == 1):
            self.password1 = self.textbox2.text()
            if (self.password == self.password1):
                f = open('login.txt', 'w')
                f.write(self.username)
                f.write(self.password)
                f.close()
            else:
                QMessageBox.about(self, "Title", "Passwords Don't Match")
                self.flag = 0 
                return 
            self.flag = 0
            self.closeAllWindows()
            sys.exit() 
        else:
            self.auth()
            self.closeAllWindows()
            sys.exit() 
 
                                                                                     
    def mouseMoveEvent(self, event):
        cursor = QCursor()
        if(event.y() < 10):
            cursor.setPos(1920,1080)
        
    def register(self):
        self.textbox2.show()
        self.flag = 1

    def auth(self):
        f = open('login.txt', 'r')
        x = f.readline()
        print(x) 
        print(self.username + self.password)
        if(self.username + self.password == x):
                return True 
        else:
                return False
        return False 
           
              
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(imgpath=sys.argv[1])
    app.setOverrideCursor(QCursor(Qt.BlankCursor))     
    sys.exit(app.exec_())
    


