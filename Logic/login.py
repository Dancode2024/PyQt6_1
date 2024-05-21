import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QMessageBox    
)

from PyQt6.QtGui import QFont

from  form import FormWindows

from  register import RegistrationForm

class login (QWidget) :
    def __init__ (self):
        super().__init__ ()    
        self.initUI ()
        
    def initUI (self):
        self.setGeometry(450,300,300,270)
        self.setWindowTitle("Login")
        self.generateUI()
        self.show()
        
    def generateUI (self):
        self.is_logged_in = False
        
        user = QLabel(self)
        user.setText("Username: ")
        user.setFont(QFont ('Arial',10))
        user.move(20,54)
        
        self.user  = QLineEdit(self)
        self.user.resize(180,24)
        self.user.move(90,44)
        
        password = QLabel(self)
        password.setText("Password: ")
        password.setFont(QFont ('Arial',10))
        password.move(20,86)
        
        self.password = QLineEdit(self)
        self.password.resize(180,24)
        self.password.move(90,82)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        
        # btn chk
        self.chk = QCheckBox(self)
        self.chk.setText("Show Password ")
        self.chk.move(90,110)
        self.chk.toggled.connect(self.viewPassword)
        
        # btn logout
        login = QPushButton(self)
        login.setText("Login")
        login.resize(250,35)
        login.move(20, 140)
        login.clicked.connect(self.login_user)
        
        #btn register
        register = QPushButton(self)
        register.setText("Register ")
        register.resize(250,35)
        register.move(20,180)
        register.clicked.connect(self.register_user)
        
    #FUNCIONES
    
    #VER CONTRASEÑA
    def viewPassword(self, password):
        if password : 
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else : 
            self.password.setEchoMode(QLineEdit.EchoMode.Password)
            
    #INICIAR SESION
    def login_user(self):
        users =  []
        user_path = "login.txt"  
        try :
            with open(user_path, 'r') as f:
                for line in f:
                    users.append(line.strip("\n"))
                login_information = f'{self.user.text()},{self.password.text()}'
        
            if login_information in users:
                QMessageBox.information(self, "Inicio sesión",
                "Inicio sesión con exito",
                QMessageBox.StandardButton.Ok, 
                QMessageBox.StandardButton.Ok)
                self.is_logged_in = True
                self.close()
                self.open_form_windows()     
            else: 
                QMessageBox.warning(self, "Error",
                "Usuario o contraseña incorrectos",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error',f'LA bd no existe: {e}',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
            
    #REGISTRAR USUARIO
    def register_user(self):
        self.new_register = RegistrationForm()
        self.new_register.show()
    
    def open_form_windows(self):
        self.form_windows = FormWindows()
        self.form_windows.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = login()
    sys.exit(app.exec())
        
        
        
        