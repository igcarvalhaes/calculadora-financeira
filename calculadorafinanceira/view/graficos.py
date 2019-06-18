# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/graficos.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxGraficos = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGraficos.setGeometry(QtCore.QRect(0, 0, 800, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxGraficos.sizePolicy().hasHeightForWidth())
        self.groupBoxGraficos.setSizePolicy(sizePolicy)
        self.groupBoxGraficos.setTitle("")
        self.groupBoxGraficos.setObjectName("groupBoxGraficos")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxGraficos)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def continueUiSetup(self, resultadoCalculo):
        jurosPagoSac = sum(x[3] for x in resultadoCalculo.getResultadoSac()[1:-1])
        jurosPagoPrice = sum(x[3] for x in resultadoCalculo.getResultadoPrice()[1:-1])

        static_canvas = FigureCanvas(Figure())
        self.gridLayout.addWidget(static_canvas, 0, 0, 1, 1)

        objects = ('SAC', 'Price')
        y_pos = np.arange(len(objects))
        performance = [jurosPagoSac, jurosPagoPrice]

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.bar(y_pos, performance, align='center', alpha=0.5)
