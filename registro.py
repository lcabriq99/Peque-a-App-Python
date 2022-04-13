import csv
import sys

from PyQt5.QtGui import QBrush, QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QFileDialog, QLabel

from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QFileDialog, QLabel


class registro(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(registro, self).__init__(*args, **kwargs)

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




        self.setWindowTitle("Interfaz")
        self.setFixedSize(600, 500)
        self.button1 = QPushButton(self, text="Registrase")
        self.button1.move(100, 400)
        self.button1.setFixedWidth(100)
        self.button1.setFixedHeight(28)
        self.button1.clicked.connect(self.registrar)

        ###BOTON VOLVER DE IMPORTAR###
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Volver')
        self.pushButton.clicked.connect(self.goMainWindow)
        self.pushButton.setFixedWidth(100)
        self.pushButton.setFixedHeight(28)
        self.pushButton.move(240, 400)

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
        self.lineEditUsuario.setFixedWidth(238)
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
        frameContrasenia.setFixedHeight(28)
        frameContrasenia.move(60, 340)

        self.lineEditContrasenia = QLineEdit(frameContrasenia)
        self.lineEditContrasenia.setFrame(False)
        self.lineEditContrasenia.setEchoMode(QLineEdit.Password)
        self.lineEditContrasenia.setTextMargins(8, 0, 4, 1)
        self.lineEditContrasenia.setFixedWidth(238)
        self.lineEditContrasenia.setFixedHeight(26)
        self.lineEditContrasenia.move(40, 1)

    def registrar(self):

        usuario = self.lineEditUsuario.text()
        contrasenia = self.lineEditContrasenia.text()

        self.lineEditUsuario.clear()
        self.lineEditContrasenia.clear()

        f = open("usuario.txt", "a")
        f.write(usuario)
        f.write("\n")
        f.close()

        f2 = open("contrasenia.txt", "a")
        f2.write(contrasenia)
        f2.write("\n")
        f2.close()





    def ventana_salir(self):
        print("Salir")

        self.close()

    def goMainWindow(self):
        print("salir")

        self.close()





if __name__ == '__main__':
    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    background = QPixmap('D:\salsa.jpg')



    aplicacion.setFont(fuente)

    ventana2 = registro()
    pal = ventana2.palette()
    pal.setBrush(QPalette.Background, QBrush(background))
    ventana2.setPalette(pal)
    ventana2.show()



    sys.exit(aplicacion.exec_())