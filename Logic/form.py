import sys
from PyQt6.QtWidgets import (QApplication, 
                            QWidget,
                            QLabel,
                            QPushButton,
                            QDateEdit,
                            QLineEdit,
                            QComboBox,
                            QFormLayout
                            ,QHBoxLayout,
                            QVBoxLayout,
                            QMessageBox)


from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QDate


class FormWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.registerForm()
        
        
    def registerForm(self):
        self.setGeometry(500, 500, 290, 270)
        self.setWindowTitle("Formulario")
        self.generateRegistration()
        self.show()
        
    def generateRegistration(self):
        title = QLabel("Registration")
        title.setFont(QFont("Arial", 12))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.name = QLineEdit()
        self.name.setPlaceholderText('Nombre')
        
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText('Apellido')
        
        self.age = QLineEdit()
        self.age.setPlaceholderText('Edad')
        
        self.options = QComboBox()
        self.options.addItems(['Hombre', 'Mujer'])
        
        self.address = QLineEdit()
        self.address.setPlaceholderText('Direccion')
        
        self.phone = QLineEdit()
        self.phone.setPlaceholderText('Telefono')
        
        self.email = QLineEdit()
        self.email.setPlaceholderText('Correo')
        
        self.fecha = QDateEdit()
        self.fecha.setDisplayFormat("yyyy-MM-dd")
        self.fecha.setMaximumDate(QDate.currentDate())
        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(QDate.currentDate())
        
        register_btn =  QPushButton()
        register_btn.setText("Guardar")
        register_btn.resize(100,30)
        register_btn.move(20,150)
        register_btn.clicked.connect(self.create_user)
        
        cancel_btn = QPushButton()
        cancel_btn.setText("Cancelar")
        cancel_btn.resize(100,30)
        cancel_btn.move(170,150)
        cancel_btn.clicked.connect(self.cancel_user)
        
        one_h_box = QHBoxLayout()
        one_h_box.addWidget(self.name)
        one_h_box.addWidget(self.last_name)
        
        
        edad_label= QLabel("Edad: ")
        
        genero_label= QLabel("Genero: ")
       
        
        three_h_box = QHBoxLayout()
        three_h_box.addWidget(register_btn)
        three_h_box.addWidget(cancel_btn)
        
        main_form = QFormLayout()
        main_form.addRow(title)
        main_form.addRow("Nombre: ",one_h_box,)
        main_form.addRow(edad_label, self.age)
        main_form.addRow(genero_label, self.options)
        main_form.addRow("date: ", self.fecha)
        main_form.addRow("address: ", self.address)
        main_form.addRow("phone: ", self.phone)
        main_form.addRow("email: ", self.email)
        main_form.addRow(three_h_box)
        
        self.setLayout(main_form)
        
    def create_user(self):
        user_path = "form.txt"
        nombre =  self.name.text()
        apellido = self.last_name.text()
        edad = self.age.text()
        opcion = self.options.currentText()
        fecha = self.fecha.text()
        direccion = self.address.text()
        telefono = self.phone.text()
        correo = self.email.text()
        
        if nombre == '' or apellido == '' or edad == '' or opcion == '' or fecha == '' or direccion == '' or telefono == '' or correo == '':        
            QMessageBox.warning(self, "Error", "Ingrese datos validos"
                                 , QMessageBox.StandardButton.Close,
                                 QMessageBox.StandardButton.Close)   
        else:
            try:
                with open(user_path, 'a+') as f:
                    f.write(f"{nombre},{apellido},{edad},{opcion},{fecha},{direccion},{telefono},{correo}\n")
                    
                    QMessageBox.information(self, "Exito", "Registro creado",
                                            QMessageBox.StandardButton.Close,
                                            QMessageBox.StandardButton.Close)
                    self.close()
            except Exception as e:
                print(f"Error al escribir en el archivo: {e}") 
                
    def cancel_user(self):
        self.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

        