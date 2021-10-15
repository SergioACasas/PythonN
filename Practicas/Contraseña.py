# -*- coding: utf-8 -*
from PyQt5 import QtCore, QtGui, QtWidgets
import string
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 20))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 221, 101))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(132, 30, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        #Cambio minimo y me fijo si el enter se presiona y es registrado
        self.lineEdit.setPlaceholderText("N° ")
        self.lineEdit.returnPressed.connect(self.showtext)

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        #AL fin connectaste una funcion al evento Clicked

        #self.pushButton.clicked.connect(self.newran)
        #self.pushButton_2.clicked.connect(self.CopytoClipboard)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 180, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        #Esta linea oculta lo escrito
        #self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.lineEdit_2.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #-------------------------------------Si se puede dejar al final pero dentro del loop------------------------------------------
        self.lineEdit_2.setReadOnly(True)
        self.pushButton.clicked.connect(self.newran)
        self.pushButton_2.clicked.connect(self.CopytoClipboard)
    #----------------------------------------------------------------------------------------------------------------------------------
    def showtext(self):
        att = self.lineEdit.text()
        print(att)
    # RECUERDA siempre se llama el tree 'SELF' de alli te manejas para adelante
    def newran(self):
        sw = ""
        for i in range(int(self.lineEdit.text())):
            sw = sw + random.choice(string.ascii_letters+string.digits)
        self.lineEdit_2.setText(sw)
        return
    #Con esta funcion copiamos al clip de notas de windows
    def CopytoClipboard(self):
        cb= QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.lineEdit_2.text(),mode=cb.Clipboard)
    #----------------------------------------------------------------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Copia"))
        self.label.setText(_translate("MainWindow", "Generador de Contraseña"))
        self.groupBox.setTitle(_translate("MainWindow", "Hola!"))
        self.pushButton.setText(_translate("MainWindow", "Ingresar"))
        self.label_2.setText(_translate("MainWindow", "Tamaño de contraseña"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())