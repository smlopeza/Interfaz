# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox,QAction, QFileDialog
# import Script_entradas as SE
# from Q3P3 import Modelo3_
from functools import partial

import pandas as pd
import numpy as np
import datetime as dt
import Script_entradas as SE
from copy import deepcopy

""" Este incluye lluvia entonces es trihorario"""

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]



def showdialog(self):

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowIcon(QtGui.QIcon("gear2.jpg"))

    msg.setText("Pronóstico Guardado")
    #msg.setInformativeText("This is additional information")
    msg.setWindowTitle("Status")
    #msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


class Ui_MainWindow(object):
    def __init__( self ):
        '''
        Initialize the super class
        '''
        super().__init__()
        # self.text_Q = self.SingleBrowse2()
        # self.text_P = self.FolderBrowse2()
    # def __init__(self):
    #
    #     self.text_Q = self.Q3P3_Q_toolButton.clicked.connect(self.SingleBrowse2)
    #     self.text_P = self.Q3P3_P_toolButton.clicked.connect(self.FolderBrowse2)

    def SingleBrowse2(self):
        filePaths,_ = QFileDialog.getOpenFileNames(self, 'Abrir archivo', "home",'*.csv')
        # text = SE.Lectura_Q(filePaths[0])
        self.text_Q = filePaths[0]
        # print (type(text))
        # print (text)
        # return text
        # return filePaths[0]

    def FolderBrowse2(self):
        filePaths = QFileDialog.getExistingDirectory(self, ("Seleccionar carpeta"),  "home")
        # text = SE.Read_WRF_Amoya(filePaths+'/')
        self.text_P = filePaths+'/'
        # print (type(text))
        # print (text)
        # return text
        # return filePaths+'/'


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.setWindowIcon(QtGui.QIcon("gear2.jpg"))
        self.centralwidget.setObjectName("centralwidget")


        # ------------ Boton que selecciona tipo de modelo -------------------
        self.Q3P3_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.Q3P3_radioButton.setGeometry(QtCore.QRect(20, 30, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Q3P3_radioButton.setFont(font)
        self.Q3P3_radioButton.setObjectName("Q3P3_radioButton")

        self.Q1_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.Q1_radioButton.setGeometry(QtCore.QRect(20, 160, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Q1_radioButton.setFont(font)
        self.Q1_radioButton.setObjectName("Q1_radioButton")


        # ---------- Espacios blanco para subida de archivos ------------------
        self.Q3P3_Q_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Q3P3_Q_textEdit.setGeometry(QtCore.QRect(69, 70, 401, 31))
        self.Q3P3_Q_textEdit.setObjectName("Q3P3_Q_textEdit")

        self.Q3P3_P_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Q3P3_P_textEdit.setGeometry(QtCore.QRect(69, 110, 401, 31))
        self.Q3P3_P_textEdit.setObjectName("Q3P3_P_textEdit")

        self.Q1_Q_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Q1_Q_textEdit.setGeometry(QtCore.QRect(70, 190, 401, 31))
        self.Q1_Q_textEdit.setObjectName("Q1_Q_textEdit")

        #------------ Botones que seleccionan los archivos ------------------
        self.Q3P3_Q_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.Q3P3_Q_toolButton.setGeometry(QtCore.QRect(440, 70, 31, 31))
        self.Q3P3_Q_toolButton.setObjectName("Q3P3_Q_toolButton")
        # text_Q = self.Q3P3_Q_toolButton.clicked.connect(self.SingleBrowse2)
        self.Q3P3_Q_toolButton.clicked.connect(self.SingleBrowse2)
        #print (text)

        self.Q3P3_P_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.Q3P3_P_toolButton.setGeometry(QtCore.QRect(440, 110, 31, 31))
        self.Q3P3_P_toolButton.setObjectName("Q3P3_P_toolButton")
        # text_P = self.Q3P3_P_toolButton.clicked.connect(self.FolderBrowse2)
        self.Q3P3_P_toolButton.clicked.connect(self.FolderBrowse2)

        self.Q1_Q_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.Q1_Q_toolButton.setGeometry(QtCore.QRect(440, 190, 31, 31))
        self.Q1_Q_toolButton.setObjectName("Q1_Q_toolButton")
        text_Q1 = self.Q1_Q_toolButton.clicked.connect(self.SingleBrowse2)


        # ---------------- Boton que verifica calidad ------------------------
        self.Calidad_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Calidad_Button.setGeometry(QtCore.QRect(40, 260, 211, 28))
        self.Calidad_Button.setObjectName("Calidad_Button")


        # ------------- El boton que corre el modelo ----------------------
        self.Pronostico_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Pronostico_Button.setGeometry(QtCore.QRect(270, 260, 201, 28))
        self.Pronostico_Button.setObjectName("Pronostico_Button")




        # Pron = self.Pronostico_Button.clicked.connect(lambda: self.Modelo3_(text_Q,text_P))###############################################
        self.Pronostico_Button.clicked.connect(self.Modelo3_)###############################################
        # Mierda_pron = self.Pronostico_Button.clicked.connect(
        #                 self.Modelo3_(SE.Lectura_Q(self.text_Q),
        #                               SE.Read_WRF_Amoya(self.text_P)))###############################################
        #Pron = self.Pronostico_Button.clicked.connect(partial(Modelo3_,text_Q,text_P))# Modelo3_(text_Q,text_P))



        # --------------Espacio para mostrar la grafica ----------------------
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 330, 441, 171))
        self.graphicsView.setObjectName("graphicsView")


        # -------------- Tablita para mostrar valores -----------------------
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 520, 261, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(270, 520, 21, 161))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")


        # ------------ Boton Historico checkear para guardar -----------------
        self.Historico_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Historico_checkBox.setGeometry(QtCore.QRect(300, 620, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.Historico_checkBox.setFont(font)
        self.Historico_checkBox.setObjectName("Historico_checkBox")


        # ---------------- Boton pa guardar pronostico ---------------------
        self.Save_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Button.setGeometry(QtCore.QRect(300, 650, 161, 31))
        self.Save_Button.setObjectName("Save_Button")
        self.Save_Button.clicked.connect(showdialog)


        #------------------------------LABELS ----------------------------------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(41, 118, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 75, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 310, 431, 16))
        self.label_4.setObjectName("label_4")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pronostico Amoya "))
        self.Historico_checkBox.setText(_translate("MainWindow", "Guardar como historico"))
        self.Q3P3_radioButton.setText(_translate("MainWindow", "Modelo Q3P3"))
        self.Q1_radioButton.setText(_translate("MainWindow", "Modelo Q1"))
        self.Calidad_Button.setText(_translate("MainWindow", "Verificar Calidad"))
        self.Save_Button.setText(_translate("MainWindow", "Guardar Pronostico"))
        self.Pronostico_Button.setText(_translate("MainWindow", "Correr Pronostico"))
        self.label.setText(_translate("MainWindow", "P"))
        self.label_2.setText(_translate("MainWindow", "Q"))
        self.label_3.setText(_translate("MainWindow", "Q"))
        self.label_4.setText(_translate("MainWindow", "Resultado Pronóstico Caudal a 72 horas"))
        self.Q1_Q_toolButton.setText(_translate("MainWindow", "..."))
        self.Q3P3_Q_toolButton.setText(_translate("MainWindow", "..."))
        self.Q3P3_P_toolButton.setText(_translate("MainWindow", "..."))

    def Modelo3_(self):

        Caudales_Amoya = SE.Lectura_Q(self.text_Q)
        PPT = SE.Read_WRF_Amoya(self.text_P)
        print (Caudales_Amoya)
        #PPT = SE.Read_WRF_Amoya(ruta_ppt)
        #Caudales_Amoya = SE.Lectura_Q(ruta_q)

        #Hora_format = dt.datetime.now()

        Hora_format = dt.datetime.strptime('2019-06-07 07:00:00','%Y-%m-%d %H:%M:%S')
        hrs_disp = np.arange(1,24,3)
        nearest_hour = find_nearest(hrs_disp,Hora_format.hour)
        date_loc = dt.datetime.strptime(str(Hora_format.date())+' '+ "%02d" % nearest_hour+':00:00','%Y-%m-%d %H:%M:%S')

        entradas=np.zeros((1,5))

        Values_Q = []
        for i in [9,6,3]:
            Values_Q.append(Caudales_Amoya.loc[date_loc-dt.timedelta(hours=i)].values[0])

        Fechas_pronostico = PPT[date_loc:].index
        self.Fechas_pronostico = PPT[date_loc:].index
        """
        for Date in Fechas_pronostico:

            print (Date)
            entradas[:,0] = Values_Q[-3]
            entradas[:,1] = Values_Q[-2]
            entradas[:,2] = Values_Q[-1]
            entradas[:,3] = PPT.loc[Date-dt.timedelta(hours=6)].values
            entradas[:,4] = PPT.loc[Date-dt.timedelta(hours=3)].values

            rn = CargarPMC('/mnt/c/Users/Silvana M/Documents/Contratos/Gotta_Amoya/00_FINAL/01_SCRIPTS/Redes/PorHorizonte/Q3P3/model')
            val_pron=rn.predict(entradas)[:,0]
            Values_Q = np.append(Values_Q, val_pron)

        Pronostico = pd.DataFrame({'Caudal_pronosticado':Values_Q[-len(Fechas_pronostico):]},index= Fechas_pronostico)
        #if ruta_save != None:
        #    Pronostico.to_csv(ruta_save+'.csv')
        """

        # return Fechas_pronostico
