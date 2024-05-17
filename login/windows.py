from PyQt6.QtWidgets import (QDialog, QLabel, QWidget,
                             QMessageBox)

from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):     #x  #y  #ancho #largo
    
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle("Vista Principal")
        self.generar_contenido()
        
    def generar_contenido(self):
        image_path = "foto.png"
        
        try:
            with open(image_path) as f:
                image_label =  QLabel(self)
                image_label.setPixmap(QPixmap(image_path))
        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error',f'La imagen no existe',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self, 'Error',f'{e}',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)