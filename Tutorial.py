#!/usr/bin/env python
#-*- coding:utf-8 -*-

###############################################################
# Cargarlo directamente                                       
###############################################################
"""
import sys
from PyQt5 import QtWidgets, uic
  
app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()



import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
"""

###############################################################
# Despues de convertirlo en python                                      
###############################################################

import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow

#from Main_backup import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

