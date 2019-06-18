import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class GraficoFinanciamento:
    
    def montarGraficoJurosPagos(self, resultadoCalculo):
        jurosPagoSac = sum(x[3] for x in resultadoCalculo.getResultadoSac()[1:-1])
        jurosPagoPrice = sum(x[3] for x in resultadoCalculo.getResultadoPrice()[1:-1])
        
        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
