import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap

class Window(QWidget):

    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("Cálculo velocidad promedio")
        self.setGeometry(950, 100, 350, 530)
        self.mostrarGUI()

    def mostrarGUI(self):
        # Titutlo de la parte principal
        self.title = QLabel("Calculo velocidad promedio", self)
        self.title.setStyleSheet("color:blue;font-size:18px;font-weight:bold;")
        self.title.move(45, 10)

        # Imagen
        self.imagen = QLabel(self)
        self.imagen.setPixmap(QPixmap('carrito.png').scaled(160, 160))
        self.imagen.move(170, 85)

        # Leer distancia
        self.distancia = QLabel("Distancia (mt):", self)
        self.distancia.move(30, 60)
        self.distancia1 = QLineEdit(self)
        self.distancia1.move(30, 80)
        self.distancia1.setPlaceholderText("Distancia en metros")

        # Leer tiempo
        self.tiempo = QLabel("Tiempo (s):", self)
        self.tiempo.move(30, 120)
        self.tiempo1 = QLineEdit(self)
        self.tiempo1.move(30, 140)
        self.tiempo1.setPlaceholderText("Cantidad de tiempo")


        self.resultado_velocidad = QLabel("Velocidad m/s", self)
        self.resultado_velocidad.move(30, 180)

        self.resultado_velocidadval = QLabel("0 m/s", self)
        self.resultado_velocidadval.move(30, 200)

        # Button de guardar
        self.guardar_boton = QPushButton("Calcular", self)
        self.guardar_boton.move(30, 240)

        # Captura el evento del clic
        self.guardar_boton.clicked.connect(self.calcularVelocidad)


        self.show()

    def calcularVelocidad(self):

        valor1 = self.distancia1.text()
        valor2 = self.tiempo1.text()

        if(valor1.isnumeric() and valor2.isnumeric()):
            val1 = int(valor1)
            val2 = int(valor2)

            if(val1 > 0 and val1 > 0):
                #QMessageBox.information(self, "Información", "mayores a 0")
                self.distancia = val1 / val2
                #print(distancia)
            else:
                QMessageBox.information(self, "Información", "Digite un valor mayor a 0")
        else:
            QMessageBox.information(self, "Información", "Digite un valor numérico")

        self.resultado_velocidadval.setText(str(self.distancia) + "mt/s")
        self.resultado_velocidadval.adjustSize()

        # Limpiar los campos
        self.distancia1.clear()
        self.tiempo1.clear()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

main()