import sys
from PyQt6.QtWidgets import (QApplication,QLabel,
QWidget,QLineEdit,QLabel, QPushButton,QLabel,QCheckBox,QMessageBox)
from PyQt6.QtGui import QFont

from register import RegistrationForm
from windows import MainWindow
#POO

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):     #x  #y  #ancho #largo
        self.setGeometry(300, 300, 300, 270)
        self.setWindowTitle('Login')
        #self.setWindowIcon(QIcon('icono.png'))
        self.generatorUI()
       
        self.show()
        
    def generatorUI(self):
       self.is_logged_in = False
       
       #input username
       user_label= QLabel(self)
       user_label.setText('Usuario: ')   
       user_label.setFont(QFont('Arial',11)) 
       user_label.move(20,54) 
       
       #method para acceder a la variable
       self.user_input = QLineEdit(self)
       self.user_input.resize(180,24)
       self.user_input.move(90,44)
        
       pssword_label= QLabel(self)
       pssword_label.setText('Password:')   
       pssword_label.setFont(QFont('Arial',10)) 
       pssword_label.move(20,86) 
       
       #input password
       self.pssword_input = QLineEdit(self)
       self.pssword_input.resize(180,24)
       self.pssword_input.move(90,82)
       #ocultar password
       self.pssword_input.setEchoMode(
           QLineEdit.EchoMode.Password)
       
       #method para acceder a la variable
            
       self.chkword_input = QCheckBox(self)
       self.chkword_input.setText('Mostrar Password')
       self.chkword_input.move(90,110)
       self.chkword_input.toggled.connect(self.view_chkword)
       
       login_button = QPushButton(self)
       login_button.setText('Login')
       login_button.resize(250,35)
       login_button.move(20,140)
       login_button.clicked.connect(self.login)
       
       register_button = QPushButton(self)
       register_button.setText('Register')
       register_button.resize(250,35)
       register_button.move(20,180)
       register_button.clicked.connect(self.register_user)
       
       
    def view_chkword(self, chkword):
        if chkword:
            self.pssword_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.pssword_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    def login(self):
        users = []
        user_path = "user.txt"
        
        try:
            with open(user_path, 'r') as f:
                for line in f:
                    users.append(line.strip("\n"))
            login_information = f'{self.user_input.text()},{self.pssword_input.text()}'
            
            if login_information in users:
                QMessageBox.information(self, "Inicio sesión",
                "Inicio sesión con exito",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.is_logged_in = True
                self.close()
                self.open_main_window()
                
            else:
                QMessageBox.warning(self, "Error",
                "Usuario o contraseña incorrectos",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
                                        
            
        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error',f'LA bd no existe: {e}',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
    
    def register_user(self):
        self.new_user_form = RegistrationForm()
        self.new_user_form.show()
        
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        
       
     
#construct
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())   
