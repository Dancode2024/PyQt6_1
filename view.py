import sys
from PyQt6.QtWidgets import QApplication, QWidget

#POO

class Ventana(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()
        
    def initUI(self):     #x  #y  #ancho #largo
        self.setGeometry(300, 300, 220, 300)
        self.setWindowTitle('Ventana')
        self.show() 
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Ventana()
    sys.exit(app.exec()) # ejecuta la ventana