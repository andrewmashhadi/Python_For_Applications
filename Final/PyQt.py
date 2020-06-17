#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initPolyInfo()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Final Widget')
        self.setGeometry(0, 0, 600, 400)
        self.show()
        
    def initPolyInfo(self):
        self.vs = []
        self.doubleClicked = False
        
    def paintEvent(self, event):
        qp = QPainter()
        
        qp.begin(self)
        
        white_bg = QColor(255, 255, 255)
        
        qp.setPen(white_bg)
        qp.setBrush(white_bg)
        qp.drawRect(0, 0, self.width(), self.height())
        
        if len(self.vs) > 1:         
            self.drawAllLines(qp)
        
        qp.end()
        
    def drawAllLines(self, qp):
        for i in range(1, len(self.vs)):
            x1, y1 = self.vs[i-1]
            x2, y2 = self.vs[i]
            qp.setPen(QColor(0, 0, 255))
            qp.setBrush(QColor(0, 0, 255))
            qp.drawLine(x1, y1, x2, y2)      
        
    def mousePressEvent(self, e):
        if self.doubleClicked:
            self.vs.clear()
            self.doubleClicked = False
            
        self.vs.append((e.x(), e.y()))
        self.update()
        
    def mouseDoubleClickEvent(self, e):
        self.vs.append((e.x(), e.y()))
        self.vs.append(self.vs[0])
        self.doubleClicked = True
        self.update()
        

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

main()