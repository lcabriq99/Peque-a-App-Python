import csv
import sys
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QBrush, QPalette, QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QFileDialog, QLabel


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.setWindowTitle("Interfaz")
        self.setFixedSize(600, 500)

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
        self.button1 = QPushButton(self, text="Exportar 1")
        self.button1.move(190, 190)
        self.button1.setFixedWidth(190)
        self.button1.setFixedHeight(45)
        self.button1.clicked.connect(self.ventana_importar)
        self.button2 = QPushButton(self, text="Exportar 2")
        self.button2.move(190, 270)
        self.button2.setFixedWidth(190)
        self.button2.setFixedHeight(45)
        self.button2.clicked.connect(self.ventana_filtrar)
        self.button3 = QPushButton(self, text="Exportar 3")
        self.button3.move(190, 345)
        self.button3.setFixedWidth(190)
        self.button3.setFixedHeight(45)
        self.button3.clicked.connect(self.ventana_editar)
        self.button5 = QPushButton(self, text="Volver al Login")
        self.button5.move(190, 415)
        self.button5.setFixedWidth(190)
        self.button5.setFixedHeight(45)
        self.button5.clicked.connect(self.ventana_salir)






    def ventana_importar(self):
        window1 = Window1(self)
        window1.show()

    def ventana_filtrar(self):
        window2 = Window2(self)
        window2.show()

    def ventana_editar(self):
        window3 = Window3(self)
        window3.show()


    def ventana_salir(self):
        print("Salir")

        self.close()




class Window1(QDialog):
    def __init__(self, *args, **kwargs):
        super(Window1, self).__init__(*args, **kwargs)
        self.setWindowTitle("Exportar")
        self.setFixedSize(425, 350)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(24)
        fuenteTitulo.setBold(True)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(500)
        frame.setFixedHeight(100)
        frame.move(0, 0)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(14)

        labelSubtitulo = QLabel("<font color='white'>Importar y exportar en ficheros .FIN</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(50, 40)

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Volver')
        self.pushButton.clicked.connect(self.goMainWindow)
        self.pushButton.move(300, 300)
        layoutV.addWidget(self.pushButton)

        self.labl = QLabel(self)
        self.labl0 = QLabel(self)
        self.labl1 = QLabel(self)
        self.labl2 = QLabel(self)
        self.labl3 = QLabel(self)
        self.labl.setText('Indicaciones')
        self.labl0.setText('-1. Indicar ruta a exportar')
        self.labl1.setText('-1. Seleccionar el fichero a importar')
        self.labl2.setText('-2. Solo de admite ficheros .txt')
        self.labl3.setText('-3. Seleccionar donde se quiere que se exporte el fichero')
        self.labl.move(50, 125)
        self.labl0.move(50, 145)
        self.labl1.move(50, 165)
        self.labl2.move(50, 185)
        self.labl3.move(50, 205)
        self.labl.setFont(QFont('Arial', 13))
        self.labl0.setFont(QFont('Arial', 11))
        self.labl1.setFont(QFont('Arial', 11))
        self.labl2.setFont(QFont('Arial', 11))
        self.labl3.setFont(QFont('Arial', 11))
        ###BOTON VOLVER DE Prueba###

        self.pushButton = QPushButton(self)
        self.pushButton.setText('Importar fichero')
        self.pushButton.clicked.connect(self.prueba)
        self.pushButton.move(50, 300)

        labelUsuario = QLabel("Ruta a exportar", self)
        labelUsuario.setFont(QFont('Arial', 11))
        labelUsuario.move(50, 240)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(50, 260)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)

    def prueba(self):
        ruta = self.lineEditUsuario.text()
        self.lineEditUsuario.clear()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        nombreFichero, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                       "All Files (*);;Python Files (*.py)", options=options)

        f = open(nombreFichero, "r")
        f2 = open(ruta + '\FicheroExportado.txt', "w")

        while (True):
            linea = f.readline()
            cabecera = linea[0:3]
            cabecera = cabecera.strip()

            nombre = linea[3:14]
            nombre = nombre.strip()

            apellido1 = linea[14:28]
            apellido1 = apellido1.strip()

            apellido2 = linea[28:45]
            apellido2 = apellido2.strip()

            provincia = linea[45:60]
            provincia = provincia.strip()

            codigoPostal = linea[60:68]
            codigoPostal = codigoPostal.strip()

            valorCatastral = linea[68:74]
            valorCatastral = valorCatastral.strip()

            fechaCreacionFichero = linea[74:88]
            fechaCreacionFichero = fechaCreacionFichero.strip()

            horaCreacionFichero = linea[88:100]
            horaCreacionFichero = horaCreacionFichero.strip()

            localidad = linea[100:127]
            localidad = localidad.strip()

            numViviendas = linea[127:131]
            numViviendas = numViviendas.strip()

            calle = linea[131:148]
            calle = calle.strip()

            numero = linea[148:154]
            numero = numero.strip()

            deudas = linea[155:160]
            deudas = deudas.strip()

            fechaNacimiernto = linea[165:185]
            fechaNacimiernto = fechaNacimiernto.strip()

            superficiekm2 = linea[185:192]
            superficiekm2 = superficiekm2.strip()

            fechaPublicacionOrdenModulos = linea[194:210]
            fechaPublicacionOrdenModulos = fechaPublicacionOrdenModulos.strip()

            codigoEntidadColaboradora = linea[215:250]
            codigoEntidadColaboradora = codigoEntidadColaboradora.strip()

            codigoDelegacionMEH = linea[275:300]
            codigoDelegacionMEH = codigoDelegacionMEH.strip()

            referenciaCatastral = linea[298:325]
            referenciaCatastral = referenciaCatastral.strip()

            if cabecera == "":
                break

            f2.write(cabecera)
            f2.write(";")
            f2.write(nombre)
            f2.write(";")
            f2.write(apellido1)
            f2.write(";")
            f2.write(apellido2)
            f2.write(";")
            f2.write(provincia)
            f2.write(";")
            f2.write(codigoPostal)
            f2.write(";")
            f2.write(valorCatastral)
            f2.write(";")
            f2.write(fechaCreacionFichero)
            f2.write(";")
            f2.write(horaCreacionFichero)
            f2.write(";")
            f2.write(localidad)
            f2.write(";")
            f2.write(numViviendas)
            f2.write(";")
            f2.write(deudas)
            f2.write(";")
            f2.write(fechaNacimiernto)
            f2.write(";")
            f2.write(superficiekm2)
            f2.write(";")
            f2.write(fechaPublicacionOrdenModulos)
            f2.write(";")
            f2.write(codigoEntidadColaboradora)
            f2.write(";")
            f2.write(codigoDelegacionMEH)
            f2.write(";")
            f2.write(referenciaCatastral)
            f2.write(";")
            f2.newlines

            if not linea:
                break

        f2.close()
        f.close()

    def goMainWindow(self):
        print("Salir")
        self.close()

class Window2(QDialog):
    def __init__(self, *args, **kwargs):
        super(Window2, self).__init__(*args, **kwargs)
        self.setWindowTitle("Ventana2")
        self.setFixedSize(425, 350)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(24)
        fuenteTitulo.setBold(True)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(500)
        frame.setFixedHeight(100)
        frame.move(0, 0)



        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(13)

        labelSubtitulo = QLabel("<font color='white'>Importar y exportar en ficheros .FIN por cabeceras</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(20, 40)

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Volver')
        self.pushButton.clicked.connect(self.goMainWindow)
        self.pushButton.move(300, 300)
        layoutV.addWidget(self.pushButton)

        self.labl = QLabel(self)
        self.labl0 = QLabel(self)
        self.labl1 = QLabel(self)
        self.labl2 = QLabel(self)
        self.labl3 = QLabel(self)
        self.labl.setText('Indicaciones')
        self.labl0.setText('-1. Indicar ruta a exportar')
        self.labl1.setText('-1. Seleccionar el fichero a importar')
        self.labl2.setText('-2. Solo de admite ficheros .txt')
        self.labl3.setText('-3. Seleccionar donde se quiere que se exporten')
        self.labl.move(50, 125)
        self.labl0.move(50, 145)
        self.labl1.move(50, 165)
        self.labl2.move(50, 185)
        self.labl3.move(50, 205)
        self.labl.setFont(QFont('Arial', 13))
        self.labl0.setFont(QFont('Arial', 11))
        self.labl1.setFont(QFont('Arial', 11))
        self.labl2.setFont(QFont('Arial', 11))
        self.labl3.setFont(QFont('Arial', 11))
        ###BOTON VOLVER DE Prueba###

        self.pushButton = QPushButton(self)
        self.pushButton.setText('Importar fichero')
        self.pushButton.clicked.connect(self.prueba2)
        self.pushButton.move(50, 300)

        labelUsuario = QLabel("Ruta a exportar", self)
        labelUsuario.setFont(QFont('Arial', 11))
        labelUsuario.move(50, 240)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(50, 260)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)




    def prueba2(self):
        ruta = self.lineEditUsuario.text()
        self.lineEditUsuario.clear()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        nombreFichero, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                           "All Files (*);;Python Files (*.py)", options=options)



        f = open(nombreFichero, "r")

        f3 = open(ruta+'\FicheroTipo01.txt', "w")
        f4 = open(ruta+'\FicheroTipo12.txt', "w")
        f5 = open(ruta+'\FicheroTipo13.txt', "w")
        f6 = open(ruta+'\FicheroTipo14.txt', "w")
        f7 = open(ruta+'\FicheroTipo16.txt', "w")
        f8 = open(ruta+'\FicheroTipo17.txt', "w")
        f9 = open(ruta+'\FicheroTipo15.txt', "w")
        f10 = open(ruta+'\FicheroTipo41.txt', "w")
        f11 = open(ruta+'\FicheroTipo46.txt', "w")
        f12 = open(ruta+'\FicheroTipo47.txt', "w")
        f13 = open(ruta+'\FicheroTipo48.txt', "w")
        f14 = open(ruta+'\FicheroTipo49.txt', "w")
        f15 = open(ruta+'\FicheroTipo90.txt', "w")

        while (True):
            linea = f.readline()

            cabecera=linea[0:3]
            cabecera=cabecera.strip()

            nombre = linea[3:14]
            nombre=nombre.strip()

            apellido1 = linea[14:28]
            apellido1=apellido1.strip()

            apellido2 = linea[28:45]
            apellido2 = apellido2.strip()

            provincia = linea[45:60]
            provincia=provincia.strip()

            codigoPostal = linea[60:68]
            codigoPostal=codigoPostal.strip()

            valorCatastral = linea[68:74]
            valorCatastral=valorCatastral.strip()

            fechaCreacionFichero = linea[74:88]
            fechaCreacionFichero=fechaCreacionFichero.strip()

            horaCreacionFichero = linea[88:101]
            horaCreacionFichero=horaCreacionFichero.strip()

            localidad = linea[98:128]
            localidad=localidad.strip()

            numViviendas = linea[127:131]
            numViviendas=numViviendas.strip()

            calle = linea[131:148]
            calle=calle.strip()

            numero = linea[148:154]
            numero=numero.strip()

            deudas = linea[155:160]
            deudas=deudas.strip()

            fechaNacimiernto = linea[165:185]
            fechaNacimiernto=fechaNacimiernto.strip()

            superficiekm2=  linea[185:192]
            superficiekm2=superficiekm2.strip()

            fechaPublicacionOrdenModulos = linea[194:210]
            fechaPublicacionOrdenModulos=fechaPublicacionOrdenModulos.strip()

            codigoEntidadColaboradora = linea[215:250]
            codigoEntidadColaboradora=codigoEntidadColaboradora.strip()

            codigoDelegacionMEH= linea[275:300]
            codigoDelegacionMEH=codigoDelegacionMEH.strip()

            referenciaCatastral = linea[298:325]
            referenciaCatastral=referenciaCatastral.strip()


            if cabecera == "":

                break
            if cabecera == "01":
                f3.write(cabecera)
                f3.write(";")
                f3.write(nombre)
                f3.write(";")
                f3.write(apellido1)
                f3.write(";")
                f3.write(apellido2)
                f3.write(";")
                f3.write(provincia)
                f3.write(";")
                f3.write(codigoPostal)
                f3.write(";")
                f3.write(valorCatastral)
                f3.write(";")
                f3.write(fechaCreacionFichero)
                f3.write(";")
                f3.write(horaCreacionFichero)
                f3.write(";")
                f3.write(localidad)
                f3.write(";")
                f3.write(numViviendas)
                f3.write(";")
                f3.write(deudas)
                f3.write(";")
                f3.write(fechaNacimiernto)
                f3.write(";")
                f3.write(superficiekm2)
                f3.write(";")
                f3.write(fechaPublicacionOrdenModulos)
                f3.write(";")
                f3.write(codigoEntidadColaboradora)
                f3.write(";")
                f3.write(codigoDelegacionMEH)
                f3.write(";")
                f3.write(referenciaCatastral)
                f3.write(";")

            if cabecera == "12":
                f4.write(cabecera)
                f4.write(";")
                f4.write(nombre)
                f4.write(";")
                f4.write(apellido1)
                f4.write(";")
                f4.write(apellido2)
                f4.write(";")
                f4.write(provincia)
                f4.write(";")
                f4.write(codigoPostal)
                f4.write(";")
                f4.write(valorCatastral)
                f4.write(";")
                f4.write(fechaCreacionFichero)
                f4.write(";")
                f4.write(horaCreacionFichero)
                f4.write(";")
                f4.write(localidad)
                f4.write(";")
                f4.write(numViviendas)
                f4.write(";")
                f4.write(deudas)
                f4.write(";")
                f4.write(fechaNacimiernto)
                f4.write(";")
                f4.write(superficiekm2)
                f4.write(";")
                f4.write(fechaPublicacionOrdenModulos)
                f4.write(";")
                f4.write(codigoEntidadColaboradora)
                f4.write(";")
                f4.write(codigoDelegacionMEH)
                f4.write(";")
                f4.write(referenciaCatastral)
                f4.write(";")

            if cabecera == "13":
                f5.write(cabecera)
                f5.write(";")
                f5.write(nombre)
                f5.write(";")
                f5.write(apellido1)
                f5.write(";")
                f5.write(apellido2)
                f5.write(";")
                f5.write(provincia)
                f5.write(";")
                f5.write(codigoPostal)
                f5.write(";")
                f5.write(valorCatastral)
                f5.write(";")
                f5.write(fechaCreacionFichero)
                f5.write(";")
                f5.write(horaCreacionFichero)
                f5.write(";")
                f5.write(localidad)
                f5.write(";")
                f5.write(numViviendas)
                f5.write(";")
                f5.write(deudas)
                f5.write(";")
                f5.write(fechaNacimiernto)
                f5.write(";")
                f5.write(superficiekm2)
                f5.write(";")
                f5.write(fechaPublicacionOrdenModulos)
                f5.write(";")
                f5.write(codigoEntidadColaboradora)
                f5.write(";")
                f5.write(codigoDelegacionMEH)
                f5.write(";")
                f5.write(referenciaCatastral)
                f5.write(";")
            if cabecera == "14":
                f6.write(cabecera)
                f6.write(";")
                f6.write(nombre)
                f6.write(";")
                f6.write(apellido1)
                f6.write(";")
                f6.write(apellido2)
                f6.write(";")
                f6.write(provincia)
                f6.write(";")
                f6.write(codigoPostal)
                f6.write(";")
                f6.write(valorCatastral)
                f6.write(";")
                f6.write(fechaCreacionFichero)
                f6.write(";")
                f6.write(horaCreacionFichero)
                f6.write(";")
                f6.write(localidad)
                f6.write(";")
                f6.write(numViviendas)
                f6.write(";")
                f6.write(deudas)
                f6.write(";")
                f6.write(fechaNacimiernto)
                f6.write(";")
                f6.write(superficiekm2)
                f6.write(";")
                f6.write(fechaPublicacionOrdenModulos)
                f6.write(";")
                f6.write(codigoEntidadColaboradora)
                f6.write(";")
                f6.write(codigoDelegacionMEH)
                f6.write(";")
                f6.write(referenciaCatastral)
                f6.write(";")
            if cabecera == "16":
                f7.write(cabecera)
                f7.write(";")
                f7.write(nombre)
                f7.write(";")
                f7.write(apellido1)
                f7.write(";")
                f7.write(apellido2)
                f7.write(";")
                f7.write(provincia)
                f7.write(";")
                f7.write(codigoPostal)
                f7.write(";")
                f7.write(valorCatastral)
                f7.write(";")
                f7.write(fechaCreacionFichero)
                f7.write(";")
                f7.write(horaCreacionFichero)
                f7.write(";")
                f7.write(localidad)
                f7.write(";")
                f7.write(numViviendas)
                f7.write(";")
                f7.write(deudas)
                f7.write(";")
                f7.write(fechaNacimiernto)
                f7.write(";")
                f7.write(superficiekm2)
                f7.write(";")
                f7.write(fechaPublicacionOrdenModulos)
                f7.write(";")
                f7.write(codigoEntidadColaboradora)
                f7.write(";")
                f7.write(codigoDelegacionMEH)
                f7.write(";")
                f7.write(referenciaCatastral)
                f7.write(";")

            if cabecera == "17":
                f8.write(cabecera)
                f8.write(";")
                f8.write(nombre)
                f8.write(";")
                f8.write(apellido1)
                f8.write(";")
                f8.write(apellido2)
                f8.write(";")
                f8.write(provincia)
                f8.write(";")
                f8.write(codigoPostal)
                f8.write(";")
                f8.write(valorCatastral)
                f8.write(";")
                f8.write(fechaCreacionFichero)
                f8.write(";")
                f8.write(horaCreacionFichero)
                f8.write(";")
                f8.write(localidad)
                f8.write(";")
                f8.write(numViviendas)
                f8.write(";")
                f8.write(deudas)
                f8.write(";")
                f8.write(fechaNacimiernto)
                f8.write(";")
                f8.write(superficiekm2)
                f8.write(";")
                f8.write(fechaPublicacionOrdenModulos)
                f8.write(";")
                f8.write(codigoEntidadColaboradora)
                f8.write(";")
                f8.write(codigoDelegacionMEH)
                f8.write(";")
                f8.write(referenciaCatastral)
                f8.write(";")

            if cabecera == "15":
                f9.write(cabecera)
                f9.write(";")
                f9.write(nombre)
                f9.write(";")
                f9.write(apellido1)
                f9.write(";")
                f9.write(apellido2)
                f9.write(";")
                f9.write(provincia)
                f9.write(";")
                f9.write(codigoPostal)
                f9.write(";")
                f9.write(valorCatastral)
                f9.write(";")
                f9.write(fechaCreacionFichero)
                f9.write(";")
                f9.write(horaCreacionFichero)
                f9.write(";")
                f9.write(localidad)
                f9.write(";")
                f9.write(numViviendas)
                f9.write(";")
                f9.write(deudas)
                f9.write(";")
                f9.write(fechaNacimiernto)
                f9.write(";")
                f9.write(superficiekm2)
                f9.write(";")
                f9.write(fechaPublicacionOrdenModulos)
                f9.write(";")
                f9.write(codigoEntidadColaboradora)
                f9.write(";")
                f9.write(codigoDelegacionMEH)
                f9.write(";")
                f9.write(referenciaCatastral)
                f9.write(";")

            if cabecera == "41":
                f10.write(cabecera)
                f10.write(";")
                f10.write(nombre)
                f10.write(";")
                f10.write(apellido1)
                f10.write(";")
                f10.write(apellido2)
                f10.write(";")
                f10.write(provincia)
                f10.write(";")
                f10.write(codigoPostal)
                f10.write(";")
                f10.write(valorCatastral)
                f10.write(";")
                f10.write(fechaCreacionFichero)
                f10.write(";")
                f10.write(horaCreacionFichero)
                f10.write(";")
                f10.write(localidad)
                f10.write(";")
                f10.write(numViviendas)
                f10.write(";")
                f10.write(deudas)
                f10.write(";")
                f10.write(fechaNacimiernto)
                f10.write(";")
                f10.write(superficiekm2)
                f10.write(";")
                f10.write(fechaPublicacionOrdenModulos)
                f10.write(";")
                f10.write(codigoEntidadColaboradora)
                f10.write(";")
                f10.write(codigoDelegacionMEH)
                f10.write(";")
                f10.write(referenciaCatastral)
                f10.write(";")

            if cabecera == "46":
                f11.write(cabecera)
                f11.write(";")
                f11.write(nombre)
                f11.write(";")
                f11.write(apellido1)
                f11.write(";")
                f11.write(apellido2)
                f11.write(";")
                f11.write(provincia)
                f11.write(";")
                f11.write(codigoPostal)
                f11.write(";")
                f11.write(valorCatastral)
                f11.write(";")
                f11.write(fechaCreacionFichero)
                f11.write(";")
                f11.write(horaCreacionFichero)
                f11.write(";")
                f11.write(localidad)
                f11.write(";")
                f11.write(numViviendas)
                f11.write(";")
                f11.write(deudas)
                f11.write(";")
                f11.write(fechaNacimiernto)
                f11.write(";")
                f11.write(superficiekm2)
                f11.write(";")
                f11.write(fechaPublicacionOrdenModulos)
                f11.write(";")
                f11.write(codigoEntidadColaboradora)
                f11.write(";")
                f11.write(codigoDelegacionMEH)
                f11.write(";")
                f11.write(referenciaCatastral)
                f11.write(";")

            if cabecera == "47":
                f12.write(cabecera)
                f12.write(";")
                f12.write(nombre)
                f12.write(";")
                f12.write(apellido1)
                f12.write(";")
                f12.write(apellido2)
                f12.write(";")
                f12.write(provincia)
                f12.write(";")
                f12.write(codigoPostal)
                f12.write(";")
                f12.write(valorCatastral)
                f12.write(";")
                f12.write(fechaCreacionFichero)
                f12.write(";")
                f12.write(horaCreacionFichero)
                f12.write(";")
                f12.write(localidad)
                f12.write(";")
                f12.write(numViviendas)
                f12.write(";")
                f12.write(deudas)
                f12.write(";")
                f12.write(fechaNacimiernto)
                f12.write(";")
                f12.write(superficiekm2)
                f12.write(";")
                f12.write(fechaPublicacionOrdenModulos)
                f12.write(";")
                f12.write(codigoEntidadColaboradora)
                f12.write(";")
                f12.write(codigoDelegacionMEH)
                f12.write(";")
                f12.write(referenciaCatastral)
                f12.write(";")

            if cabecera == "48":
                f13.write(cabecera)
                f13.write(";")
                f13.write(nombre)
                f13.write(";")
                f13.write(apellido1)
                f13.write(";")
                f13.write(apellido2)
                f13.write(";")
                f13.write(provincia)
                f13.write(";")
                f13.write(codigoPostal)
                f13.write(";")
                f13.write(valorCatastral)
                f13.write(";")
                f13.write(fechaCreacionFichero)
                f13.write(";")
                f13.write(horaCreacionFichero)
                f13.write(";")
                f13.write(localidad)
                f13.write(";")
                f13.write(numViviendas)
                f13.write(";")
                f13.write(deudas)
                f13.write(";")
                f13.write(fechaNacimiernto)
                f13.write(";")
                f13.write(superficiekm2)
                f13.write(";")
                f13.write(fechaPublicacionOrdenModulos)
                f13.write(";")
                f13.write(codigoEntidadColaboradora)
                f13.write(";")
                f13.write(codigoDelegacionMEH)
                f13.write(";")
                f13.write(referenciaCatastral)
                f13.write(";")

            if cabecera == "49":
                f14.write(cabecera)
                f14.write(";")
                f14.write(nombre)
                f14.write(";")
                f14.write(apellido1)
                f14.write(";")
                f14.write(apellido2)
                f14.write(";")
                f14.write(provincia)
                f14.write(";")
                f14.write(codigoPostal)
                f14.write(";")
                f14.write(valorCatastral)
                f14.write(";")
                f14.write(fechaCreacionFichero)
                f14.write(";")
                f14.write(horaCreacionFichero)
                f14.write(";")
                f14.write(localidad)
                f14.write(";")
                f14.write(numViviendas)
                f14.write(";")
                f14.write(deudas)
                f14.write(";")
                f14.write(fechaNacimiernto)
                f14.write(";")
                f14.write(superficiekm2)
                f14.write(";")
                f14.write(fechaPublicacionOrdenModulos)
                f14.write(";")
                f14.write(codigoEntidadColaboradora)
                f14.write(";")
                f14.write(codigoDelegacionMEH)
                f14.write(";")
                f14.write(referenciaCatastral)
                f14.write(";")

            if cabecera == "90":
                f15.write(cabecera)
                f15.write(";")
                f15.write(nombre)
                f15.write(";")
                f15.write(apellido1)
                f15.write(";")
                f15.write(apellido2)
                f15.write(";")
                f15.write(provincia)
                f15.write(";")
                f15.write(codigoPostal)
                f15.write(";")
                f15.write(valorCatastral)
                f15.write(";")
                f15.write(fechaCreacionFichero)
                f15.write(";")
                f15.write(horaCreacionFichero)
                f15.write(";")
                f15.write(localidad)
                f15.write(";")
                f15.write(numViviendas)
                f15.write(";")
                f15.write(deudas)
                f15.write(";")
                f15.write(fechaNacimiernto)
                f15.write(";")
                f15.write(superficiekm2)
                f15.write(";")
                f15.write(fechaPublicacionOrdenModulos)
                f15.write(";")
                f15.write(codigoEntidadColaboradora)
                f15.write(";")
                f15.write(codigoDelegacionMEH)
                f15.write(";")
                f15.write(referenciaCatastral)
                f15.write(";")




            if not linea:
                break
        f15.close()
        f14.close()
        f13.close()
        f12.close()
        f11.close()
        f10.close()
        f9.close()
        f8.close()
        f7.close()
        f6.close()
        f5.close()
        f4.close()
        f3.close()
        f.close()



    def goMainWindow(self):
        print("Salir")
        self.close()


class Window3(QDialog):
    def __init__(self, *args, **kwargs):
        super(Window3, self).__init__(*args, **kwargs)
        self.setWindowTitle("Exportar")
        self.setFixedSize(425, 450)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(24)
        fuenteTitulo.setBold(True)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(500)
        frame.setFixedHeight(100)
        frame.move(0, 0)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(14)

        labelSubtitulo = QLabel("<font color='white'>Importar y exportar en ficheros .FIN</font>", frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(50, 40)

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Volver')
        self.pushButton.clicked.connect(self.goMainWindow)
        self.pushButton.move(300, 410)
        layoutV.addWidget(self.pushButton)

        self.labl = QLabel(self)
        self.labl0 = QLabel(self)
        self.labl1 = QLabel(self)
        self.labl2 = QLabel(self)
        self.labl3 = QLabel(self)
        self.labl.setText('Indicaciones')
        self.labl0.setText('-1. Indicar ruta a exportar')
        self.labl1.setText('-1. Seleccionar el fichero a importar')
        self.labl2.setText('-2. Indicar referencia catastral a cambiar')
        self.labl3.setText('-3. Seleccionar donde se quiere que se exporte el fichero')
        self.labl.move(50, 125)
        self.labl0.move(50, 145)
        self.labl1.move(50, 165)
        self.labl2.move(50, 185)
        self.labl3.move(50, 205)
        self.labl.setFont(QFont('Arial', 13))
        self.labl0.setFont(QFont('Arial', 11))
        self.labl1.setFont(QFont('Arial', 11))
        self.labl2.setFont(QFont('Arial', 11))
        self.labl3.setFont(QFont('Arial', 11))
        ###BOTON VOLVER DE Prueba###

        self.pushButton = QPushButton(self)
        self.pushButton.setText('Importar fichero')
        self.pushButton.clicked.connect(self.prueba3)
        self.pushButton.move(50, 410)

        labelUsuario = QLabel("Ruta a exportar", self)
        labelUsuario.setFont(QFont('Arial', 11))
        labelUsuario.move(50, 240)

        frameUsuario = QFrame(self)
        frameUsuario.setFrameShape(QFrame.StyledPanel)
        frameUsuario.setFixedWidth(280)
        frameUsuario.setFixedHeight(28)
        frameUsuario.move(50, 260)

        self.lineEditUsuario = QLineEdit(frameUsuario)
        self.lineEditUsuario.setFrame(False)
        self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
        self.lineEditUsuario.setFixedWidth(238)
        self.lineEditUsuario.setFixedHeight(26)
        self.lineEditUsuario.move(40, 1)


        labelValorCatastral = QLabel("Valor catastral a modificar", self)
        labelValorCatastral.setFont(QFont('Arial', 11))
        labelValorCatastral.move(50, 300)

        frameValorCatastral = QFrame(self)
        frameValorCatastral.setFrameShape(QFrame.StyledPanel)
        frameValorCatastral.setFixedWidth(280)
        frameValorCatastral.setFixedHeight(28)
        frameValorCatastral.move(50, 320)

        self.lineEditValorCatastral = QLineEdit(frameValorCatastral)
        self.lineEditValorCatastral.setFrame(False)
        self.lineEditValorCatastral.setTextMargins(8, 0, 4, 1)
        self.lineEditValorCatastral.setFixedWidth(238)
        self.lineEditValorCatastral.setFixedHeight(26)
        self.lineEditValorCatastral.move(40, 1)

        labelCabecera = QLabel("Cabecera", self)
        labelCabecera.setFont(QFont('Arial', 11))
        labelCabecera.move(50, 350)

        frameCabecera = QFrame(self)
        frameCabecera.setFrameShape(QFrame.StyledPanel)
        frameCabecera.setFixedWidth(280)
        frameCabecera.setFixedHeight(28)
        frameCabecera.move(50, 370)

        self.lineEditCabecera = QLineEdit(frameCabecera)
        self.lineEditCabecera.setFrame(False)
        self.lineEditCabecera.setTextMargins(8, 0, 4, 1)
        self.lineEditCabecera.setFixedWidth(238)
        self.lineEditCabecera.setFixedHeight(26)
        self.lineEditCabecera.move(40, 1)



    def prueba3(self):
        cabeceraCambiar=self.lineEditCabecera.text()
        valorCatastralCambiar = self.lineEditValorCatastral.text()
        ruta = self.lineEditUsuario.text()
        self.lineEditUsuario.clear()
        self.lineEditValorCatastral.clear()
        self.lineEditCabecera.clear()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        nombreFichero, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                       "All Files (*);;Python Files (*.py)", options=options)
        f = open(nombreFichero, "r")
        f2 = open(ruta + '\FicheroExportado.txt', "w")

        while (True):
            linea = f.readline()

            cabecera = linea[0:3]
            cabecera = cabecera.strip()

            nombre = linea[3:14]
            nombre = nombre.strip()

            apellido1 = linea[14:28]
            apellido1 = apellido1.strip()

            apellido2 = linea[28:45]
            apellido2 = apellido2.strip()

            provincia = linea[45:60]
            provincia = provincia.strip()

            codigoPostal = linea[60:68]
            codigoPostal = codigoPostal.strip()

            valorCatastral = linea[68:74]
            valorCatastral = valorCatastral.strip()

            fechaCreacionFichero = linea[74:88]
            fechaCreacionFichero = fechaCreacionFichero.strip()

            horaCreacionFichero = linea[88:100]
            horaCreacionFichero = horaCreacionFichero.strip()

            localidad = linea[100:127]
            localidad = localidad.strip()

            numViviendas = linea[127:131]
            numViviendas = numViviendas.strip()

            calle = linea[131:148]
            calle = calle.strip()

            numero = linea[148:154]
            numero = numero.strip()

            deudas = linea[155:160]
            deudas = deudas.strip()

            fechaNacimiernto = linea[165:185]
            fechaNacimiernto = fechaNacimiernto.strip()

            superficiekm2 = linea[185:192]
            superficiekm2 = superficiekm2.strip()

            fechaPublicacionOrdenModulos = linea[194:210]
            fechaPublicacionOrdenModulos = fechaPublicacionOrdenModulos.strip()

            codigoEntidadColaboradora = linea[215:250]
            codigoEntidadColaboradora = codigoEntidadColaboradora.strip()

            codigoDelegacionMEH = linea[275:300]
            codigoDelegacionMEH = codigoDelegacionMEH.strip()

            referenciaCatastral = linea[298:325]
            referenciaCatastral = referenciaCatastral.strip()


            if cabecera == cabeceraCambiar:

                f2.write(cabecera)
                f2.write(";")
                f2.write(nombre)
                f2.write(";")
                f2.write(apellido1)
                f2.write(";")
                f2.write(apellido2)
                f2.write(";")
                f2.write(provincia)
                f2.write(";")
                f2.write(codigoPostal)
                f2.write(";")
                f2.write(valorCatastralCambiar)
                f2.write(";")
                f2.write(fechaCreacionFichero)
                f2.write(";")
                f2.write(horaCreacionFichero)
                f2.write(";")
                f2.write(localidad)
                f2.write(";")
                f2.write(numViviendas)
                f2.write(";")
                f2.write(deudas)
                f2.write(";")
                f2.write(fechaNacimiernto)
                f2.write(";")
                f2.write(superficiekm2)
                f2.write(";")
                f2.write(fechaPublicacionOrdenModulos)
                f2.write(";")
                f2.write(codigoEntidadColaboradora)
                f2.write(";")
                f2.write(codigoDelegacionMEH)
                f2.write(";")
                f2.write(referenciaCatastral)
                f2.write(";")

            if cabecera == "":
                break

            f2.write(cabecera)
            f2.write(";")
            f2.write(nombre)
            f2.write(";")
            f2.write(apellido1)
            f2.write(";")
            f2.write(apellido2)
            f2.write(";")
            f2.write(provincia)
            f2.write(";")
            f2.write(codigoPostal)
            f2.write(";")
            f2.write(valorCatastral)
            f2.write(";")
            f2.write(fechaCreacionFichero)
            f2.write(";")
            f2.write(horaCreacionFichero)
            f2.write(";")
            f2.write(localidad)
            f2.write(";")
            f2.write(numViviendas)
            f2.write(";")
            f2.write(deudas)
            f2.write(";")
            f2.write(fechaNacimiernto)
            f2.write(";")
            f2.write(superficiekm2)
            f2.write(";")
            f2.write(fechaPublicacionOrdenModulos)
            f2.write(";")
            f2.write(codigoEntidadColaboradora)
            f2.write(";")
            f2.write(codigoDelegacionMEH)
            f2.write(";")
            f2.write(referenciaCatastral)
            f2.write(";")

            if not linea:
                break

        f2.close()
        f.close()

    def goMainWindow(self):
        print("Salir")
        self.close()


if __name__ == '__main__':
    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    background = QPixmap('D:\salsa.jpg')



    aplicacion.setFont(fuente)

    ventana = MainWindow()
    pal = ventana.palette()
    pal.setBrush(QPalette.Background, QBrush(background))
    ventana.setPalette(pal)
    ventana.show()



    sys.exit(aplicacion.exec_())
