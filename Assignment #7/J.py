#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

# WHY NOT TO USE QColorDialog.getColor() ON A MAC...

# I find that after the dialog box goes away
# it misses the next mouse press.

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.p = 0
        self.show()

    def mousePressEvent(self, e):
        print('press', self.p)

    def mouseReleaseEvent(self, e):
        print('release', self.p)
        self.p += 1

    def mouseDoubleClickEvent(self, e):
        color = QColorDialog.getColor()

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

main()