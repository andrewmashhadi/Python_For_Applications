#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""


import sys

#%% Question 1
# https://doc.qt.io/qt-5/qcolordialog.html
# https://doc.qt.io/qt-5/qcolordialog.html#signals
# https://doc.qt.io/qt-5/qcolordialog.html#colorSelected
# since QColorDialog inherits from QWidget, it has a show method

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initSquare()
        self.initColorDialog()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.show()
        
    def initSquare(self):
        self.x = randint(0, 550)
        self.y = randint(0, 350)
        self.l = 50
        self.SquareColor = QColor(255, 0, 0)
        
    def initColorDialog(self):
        self.colorDialog = QColorDialog(QColor(255, 0, 0), self)
        self.colorDialog.colorSelected.connect(self.changeSquareColor)
        
    def changeSquareColor(self, new_color):
        self.SquareColor = new_color
        self.update()
        
    def paintEvent(self, event):
        qp = QPainter()
        
        qp.begin(self)
        
        white_bg = QColor(255, 255, 255)
        
        qp.setPen(white_bg)
        qp.setBrush(white_bg)
        qp.drawRect(0, 0, self.width(), self.height())
        
        qp.setPen(self.SquareColor)
        qp.setBrush(self.SquareColor)
        qp.drawRect(self.x, self.y, self.l, self.l)

        qp.end()
        
    def mousePressEvent(self, event):
        if 0 <= event.x() - self.x <= self.l and \
            0 <= event.y() - self.y <= self.l:
            self.move = True
            self.dx = event.x() - self.x
            self.dy = event.y() - self.y
        else:
            self.move = False
            
    def mouseMoveEvent(self, event):
        if self.move:
            self.x = event.x() - self.dx
            self.y = event.y() - self.dy
            self.update()
            
    def mouseDoubleClickEvent(self, event):
        if 0 <= event.x() - self.x <= self.l and \
            0 <= event.y() - self.y <= self.l:
            self.colorDialog.show()
 

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '1':
    main()


#%% Question 2
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, QThread, QEventLoop

class Thread(QThread):
    def __init__(self, parent, rate):
        super().__init__(parent)
        self.func = parent.animate
        self.rate = rate
        
    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.func)
        timer.start(self.rate)
         
        self.exec_()        
        

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()             
        self.initBall()
        self.initTimerThread()
        self.initUI()        

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.show()
        
    def initBall(self):
        self.x, self.y = 0, 0
        self.d = 30
        self.vx, self.vy = 1, 1
        self.BallColor = QColor(255, 0, 0)
        
    def initTimerThread(self):
        self.timerThread = Thread(self, 25)
        self.timerThread.start()
        
    def paintEvent(self, event):
        
        qp = QPainter()
        
        qp.begin(self)
        
        white_bg = QColor(255, 255, 255)
        
        qp.setPen(white_bg)
        qp.setBrush(white_bg)
        qp.drawRect(0, 0, self.width(), self.height())
        
        qp.setPen(self.BallColor)
        qp.setBrush(self.BallColor)
        qp.drawEllipse(self.x, self.y, self.d, self.d)

        qp.end()
        
    def animate(self):
        self.checkCollision()
        self.x += self.vx
        self.y += self.vy
        self.update()
        
    def checkCollision(self):
        if self.x >= self.width() - self.d:
            self.vx = -1
        if self.x <= 0:
            self.vx = 1
        if self.y >= self.height() - self.d:
            self.vy = -1   
        if self.y <= 0:
            self.vy = 1
            
    def closeEvent(self, e):
        self.timerThread.quit()

            

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '2':
    main()