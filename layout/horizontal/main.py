import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
    QPushButton, QLineEdit, QHBoxLayout, QMessageBox,QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumWidth(800)
        self.setFixedHeight(100)
        self.setWindowTitle('Layout Horizontal')
        self.generateLayout()
        self.show()
        
    def generateLayout(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(QLabel('Nombre'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QLabel('Email'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QLabel('Contraseña'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QLabel('Confirmar Contraseña'))
        self.layout.addWidget(QLineEdit())
        self.layout.addWidget(QPushButton('Registrar'))
        self.layout.addWidget(QPushButton('Cancelar'))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    
        
        
"""
       
        
        
        email_label = QLabel("Email Address")
        email_input = QLineEdit()
        send_button = QPushButton("Send")
        layout = QHBoxLayout()
        layout.addWidget(email_label)
        layout.addWidget(email_input)
        layout.addWidget(send_button)
        self.setLayout(layout)
        """
        