#Ejercicio1 prueba individual
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox, QGridLayout, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1 Seccion Practica Prueba Individual")
        self.setFixedSize(900, 600)
        CajaGrande = QVBoxLayout()
        CajaInferior = QHBoxLayout()
        self.caja_inferior = QStackedLayout()
        
        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)
        
        NombreUsuario = QLabel("Nombre Usuario")
        Imagen = QLabel("IMAGEN")
        TextoDescripcion = QLabel("Texto Descripcion Usuario")
        Atributo1 = QLabel("Atributo 1")
        self.Atributo1 = QLineEdit()
        formulario_registrar = QGridLayout()
        Atributo2 = QLabel("Atributo 2")
        self.Atributo2 = QLineEdit()
        Atributo3 = QLabel("Atributo 3")
        self.Atributo3 = QLineEdit()
        Atributo4 = QLabel("Atributo 4")
        self.Atributo4 = QLineEdit()
        Atributo5 = QLabel("Atributo 5")
        self.Atributo5 = QLineEdit()
        Atributo6 = QLabel("Atributo 6")
        self.Atributo6 = QLineEdit()    
        valor1 = QLabel("Valor 1")
        self.valor1 = QLineEdit()
        valor2 = QLabel("Valor 2")
        self.valor2 = QLineEdit()
        valor3 = QLabel("Valor 3")
        self.valor3 = QLineEdit()
        valor4 = QLabel("Valor 4")
        self.valor4 = QLineEdit()
        valor5 = QLabel("Valor 5")
        self.valor5 = QLineEdit()
        valor6 = QLabel("Valor 6")
        self.valor6 = QLineEdit()
        
        registrar_btn = QPushButton("OK")
        
         
        formulario_registrar.addWidget(Atributo1, 0,0)
        formulario_registrar.addWidget(self.Atributo1, 0,1)
        formulario_registrar.addWidget(valor1, 0,2)
        formulario_registrar.addWidget(self.valor1, 0,3)
        formulario_registrar.addWidget(Atributo2, 1,0)
        formulario_registrar.addWidget(self.Atributo2, 1,1)
        formulario_registrar.addWidget(valor2, 1,2)
        formulario_registrar.addWidget(self.valor2, 1,3)
        formulario_registrar.addWidget(Atributo3, 2,0)
        formulario_registrar.addWidget(self.Atributo3, 2,1)
        formulario_registrar.addWidget(valor3, 2,2)
        formulario_registrar.addWidget(self.valor3, 2,3)
        formulario_registrar.addWidget(Atributo4, 3,0)
        formulario_registrar.addWidget(self.Atributo4, 3,1)
        formulario_registrar.addWidget(valor4, 3,2)
        formulario_registrar.addWidget(self.valor4, 3,3)
        formulario_registrar.addWidget(Atributo5, 4,0)
        formulario_registrar.addWidget(self.Atributo5, 4,1)
        formulario_registrar.addWidget(valor5, 4,2)
        formulario_registrar.addWidget(self.valor5, 4,3)
        formulario_registrar.addWidget(Atributo6, 5,0)
        formulario_registrar.addWidget(self.Atributo6, 5,1)
        formulario_registrar.addWidget(valor6, 5,2)
        formulario_registrar.addWidget(self.valor6, 5,3)
        formulario_registrar.addWidget(registrar_btn, 6,3)
        
        layout.addWidget(NombreUsuario)       
        layout.addWidget(Imagen)
        layout.addWidget(TextoDescripcion)
        layout.addLayout(formulario_registrar)
        
        self.caja_inferior.addWidget(contenedor)
        
        CajaGrande.addLayout(CajaGrande)
        CajaGrande.addLayout(self.caja_inferior)
        
        
        ventana = QWidget()
        ventana.setLayout(CajaGrande)
        self.setCentralWidget(ventana)

if __name__ == "__main__":
        
    lista_usuario = [] # list()
    
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio 
    
    #sys.close(app.exec())
app.exec()
