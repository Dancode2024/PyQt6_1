import sys
from PyQt6.QtWidgets import (QApplication, QWidget, 
    QPushButton,QVBoxLayout,QVBoxLayout,QLabel,
    QLineEdit,QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):     #x  #y  #ancho #largo
        self.setMaximumHeight(700)
        self.setFixedWidth(300)
        self.setWindowTitle("Layout Vertical")
        self.generar_contenido()
        self.show()
        
    def generar_contenido(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(QLabel('Nombre'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QLabel('Email'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QLabel('Contraseña'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QLabel('Confirmar Contraseña'))
        self.layout.addWidget(QLineEdit())
        #Crear Botones
        self.btn1 = QPushButton('Registrar')
        self.btn2 = QPushButton('Cancelar')
        
        #añadir botones al layout 
        
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)

        #dar funcionalidad a los botones
        self.btn1.clicked.connect(self.registrar)
        self.btn2.clicked.connect(self.cancelar)
        
    def registrar(self):
        button = self.sender()
        QMessageBox.information(self, "Exito", 
        f'Usuario creado exitosamente',
        QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.Ok)
        
    def cancelar(self):
        self.close()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())