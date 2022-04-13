import csv
from tkinter import messagebox
import sys

import temp as temp
from PyQt5.QtGui import QBrush, QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QFileDialog, QLabel

from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)

# ===================== CLASE ventanaLogin =========================
from PyQt5.uic.properties import QtGui, QtWidgets

from Interfaz import MainWindow
from registro import registro


class ventanaLogin(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaLogin, self).__init__(parent)
 
        self.setWindowTitle("App")

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(600, 500)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(paleta)

        self.initUI()

    def initUI(self):
        # ==================== FRAME ENCABEZADO ====================

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(750)
        frame.setFixedHeight(150)
        frame.move(0, 0)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(24)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>Catastro</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(100, 40)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(16)

        labelSubtitulo = QLabel("<font color='white'>Aplicación de conversión ficheros .FIN</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(145, 90)



        # ========================================================

        labelUsuario = QLabel("Usuario", self)
        labelUsuario.setStyleSheet("font:bold;font-size: 16pt;color: #572364")
        labelUsuario.setFixedWidth(250)
        labelUsuario.move(60, 175)


        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(60, 225)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(280)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)

        # ========================================================

        labelContrasenia = QLabel("Contraseña", self)
        labelContrasenia.setFixedWidth(250)
        labelContrasenia.setStyleSheet("font:bold;font-size: 16pt;color: #572364")
        labelContrasenia.move(60, 290)



        frameContrasenia = QFrame(self)
        frameContrasenia.setFrameShape(QFrame.StyledPanel)
        frameContrasenia.setFixedWidth(280)
        frameContrasenia.setFixedHeight(55)
        frameContrasenia.move(60, 340)

        ###BOTON VOLVER DE IMPORTAR###
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Iniciar Sesión')
        self.pushButton.setFixedWidth(135)
        self.pushButton.setFixedHeight(28)
        self.pushButton.move(120, 400)
        self.pushButton.clicked.connect(self.Login)

        self.lineEditContrasenia = QLineEdit(frameContrasenia)
        self.lineEditContrasenia.setFrame(False)
        self.lineEditContrasenia.setEchoMode(QLineEdit.Password)
        self.lineEditContrasenia.setTextMargins(8, 0, 4, 1)
        self.lineEditContrasenia.setFixedWidth(280)
        self.lineEditContrasenia.setFixedHeight(26)
        self.lineEditContrasenia.move(40, 1)

        # ================== WIDGETS QPUSHBUTTON ===================

        buttonCancelar = QPushButton("Cancelar", self)
        buttonCancelar.setFixedWidth(135)
        buttonCancelar.setFixedHeight(28)
        buttonCancelar.move(205, 440)





        # ==================== PÁGINA OFICIAL DE CATASTRO =====================

        labelInformacion = QLabel("<a href='https://www.sedecatastro.gob.es?"
                                  "sub_confirmation=1'>Más información</a>.", self)
        labelInformacion.setStyleSheet("font:bold;font-size: 9pt")
        labelInformacion.setOpenExternalLinks(True)
        labelInformacion.move(450, 450)



        # ==================== SEÑALES BOTONES =====================

        ###BOTON VOLVER DE IMPORTAR###
        layoutV = QVBoxLayout()
        self.buttonRegistro = QPushButton(self)
        self.buttonRegistro.setText('Registrarse')
        self.buttonRegistro.setFixedWidth(135)
        self.buttonRegistro.setFixedHeight(28)
        self.buttonRegistro.move(275, 400)
        self.buttonRegistro.clicked.connect(self.Registro)

        buttonCancelar.clicked.connect(self.close)




    def goMainWindow(self):
        print("salir")

    def Registro(self):
        print("En registro")
        window2 = registro(self)
        window2.show()

    def Login(self):
        usuario = self.lineEditUsuario.text()
        contrasenia = self.lineEditContrasenia.text()
        f = open("usuario.txt", "r")
        f2 = open("contrasenia.txt", "r")
        while (True):
            linea = f.readline()
            linea2 = linea[:-1]

            d=(len(linea2))

            lineac = f2.readline()
            lineac2 = lineac[:-1]

            d2 = (len(lineac2))

            if d == 0:
                entrar = "vacio"
                linea2=linea2+"ghghkjgkhgkhhgkhkghj"

            if linea2 == usuario and lineac2 == contrasenia:
                entrar="si"
                window = MainWindow(self)
                window.show()

            elif usuario == "":
                QMessageBox.about(self, "Error", "Introduce el usuario")
                break

            elif contrasenia == "":
                QMessageBox.about(self, "Error", "Introduce la contraseña")
                break

            elif linea2 == usuario and lineac2 != contrasenia:
                QMessageBox.about(self, "Error", "Contraseña incorrecta")
                break

            elif linea2 == usuario and lineac2 != contrasenia:
                QMessageBox.about(self, "Error", "Usuario incorrecto")
                break
            else:
                entrar="no"


            if not linea:
                break

        f.close()
        f2.close()

        self.lineEditUsuario.clear()
        self.lineEditContrasenia.clear()


# ================================================================

if __name__ == '__main__':
    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    background = QPixmap('D:\salsa.jpg')
    # background = background.scaled(w.size(), Qt.IgnoreAspectRatio)


    aplicacion.setFont(fuente)

    ventana = ventanaLogin()
    pal = ventana.palette()
    pal.setBrush(QPalette.Background, QBrush(background))
    ventana.setPalette(pal)
    ventana.show()



    sys.exit(aplicacion.exec_())
