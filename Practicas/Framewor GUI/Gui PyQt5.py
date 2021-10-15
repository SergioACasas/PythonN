from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    # creamos la ventana ( posicion x inicial,posicion y inicial,tamaño de ancho x,tamaño de altura y)
    ventana.setGeometry(140,140,400,300)
    ventana.setWindowTitle("Titulo de ventana")
    #colocando etiquetas
    etiqueta = QtWidgets.QLabel(ventana)
    etiqueta.setText("Hola Mundo")
    etiqueta.move(50,50)


    #cerrando limpiamente la aplicacion
    ventana.show()
    sys.exit(app.exec_())

window()