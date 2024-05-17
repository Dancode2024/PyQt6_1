from PyQt6.QtWidgets import (QDialog, QLabel, QWidget,
                             QPushButton, QLineEdit, QMessageBox)

from PyQt6.QtGui import QFont, QPixmap


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.registerForm()
        self.show()
        
    def registerForm(self):
        
        self.dialog = QDialog()
        #definir titulo
        self.dialog.setWindowTitle("Registro")
        self.dialog.setFixedSize(400, 300)
        self.dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,45)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(180,24)
        self.user_input.move(90,40)
        
        
        pass1_label = QLabel(self)
        pass1_label.setText("Password: ")
        pass1_label.setFont(QFont("Arial",10))
        pass1_label.move(20,74)
        
        self.pass1_label  = QLineEdit(self)
        self.pass1_label .resize(180,24)
        self.pass1_label .move(90,70)
        self.pass1_label .setEchoMode(QLineEdit.EchoMode.Password)
        
        pass2_label = QLabel(self)
        pass2_label.setText("Password: ")
        pass2_label.setFont(QFont("Arial",10))
        pass2_label.move(20,104)
        
        self.pass2_label  = QLineEdit(self)
        self.pass2_label .resize(180,24)
        self.pass2_label .move(90,100)
        self.pass2_label .setEchoMode(QLineEdit.EchoMode.Password)
        
        create_button = QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(100,30)
        create_button.move(20,150)
        create_button.clicked.connect(self.create_user)
        
        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(100,30)
        cancel_button.move(170,150)
        cancel_button.clicked.connect(self.cancel_user)
        
    def create_user(self):
        user_path = "user.txt"
        user = self.user_input.text()
        pass1 = self.pass1_label.text()
        pass2 = self.pass2_label.text()
        
        if pass1 == '' or pass2 == '' or user == '':
            QMessageBox.warning(self, 'Error','Ingrese datos validos',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
        elif pass1 != pass2:
            QMessageBox.warning(self, 'Error','Ingrese datos validos',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(user_path, 'a+') as f:
                    f.write(f"{user},{pass1}\n")
                    print("Escritura exitosa.")
                    QMessageBox.information(self, 'Exito','Usuario creado exitosamente',
                                QMessageBox.StandardButton.Ok, 
                                QMessageBox.StandardButton.Ok)
                    self.close()
            except Exception as e:
                    print(f"Error al escribir en el archivo: {e}") 
                    
            """except FileNotFoundError as e:
                QMessageBox.warning(self, 'Error',f'LA bd no existe: ',
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)"""
                                
                               
                
                
    
    def cancel_user(self):
        self.close()
       
        