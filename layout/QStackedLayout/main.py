import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                            QTextEdit,QComboBox, QPushButton, QCheckBox, QDateEdit, QMessageBox, 
                            QStackedLayout, QFormLayout, QVBoxLayout, QGridLayout, QHBoxLayout)

from PyQt6.QtCore import Qt, QDate

from PyQt6.QtGui import QFont,QPixmap

class SlackWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI ()
        

    def initUI (self):
        self.setWindowTitle("Slack")
        self.setGeometry(300, 300, 500, 500)
        self.generateWindow()
        self.show()
        
    def generateWindow(self):
        bnt_1 =  QPushButton("Window Image")
        bnt_1.clicked.connect(self.windows  )
        btn_2 = QPushButton("Window Form")
        btn_2.clicked.connect(self.windows)
        btn_3 = QPushButton("Window Edit")
        btn_3.clicked.connect(self.windows)
        
        h_box = QHBoxLayout()
        h_box.addWidget(bnt_1)
        h_box.addWidget(btn_2)
        h_box.addWidget(btn_3)
        
        #Pagina 1
        
        title = QLabel("Pagina 1")
        title.setFont(QFont('Arial',18))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        image_1 = QLabel()
        pixmap = QPixmap("Dani.png")
        image_1.setPixmap(pixmap)
        
        #tamaño de la ventana
        windows_size = self.size()
        image_1.setMaximumSize(windows_size)
        image_1.setScaledContents(True)
        
        v_box = QVBoxLayout(self)
        v_box.addWidget(title)
        v_box.addWidget(image_1)
        
        container_1 = QWidget(self)
        container_1.setLayout(v_box)
        
        
        #Pagina 2
        
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
        
        container_2 = QWidget()
        container_2.setLayout(main_form)
        
        # Pagina 3
        
        title_3 = QLabel()
        title_3.setFont(QFont('Arial',18))
        title_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.observations = QTextEdit()
        form_3 = QFormLayout()
        form_3.addRow(title_3)
        form_3.addRow("Observaciones", self.observations)
        
        container_3 = QWidget()
        container_3.setLayout(form_3)
        
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(container_2)
        self.stacked_layout.addWidget(container_3) 
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(h_box)
        main_layout.addLayout(self.stacked_layout)
        
        self.setLayout(main_layout)
        
    def windows(self):
        btn = self.sender()
        
        if btn.text().lower() == "window image":
            self.stacked_layout.setCurrentIndex(0)
        elif btn.text().lower() == "window form":
            self.stacked_layout.setCurrentIndex(1)
        elif btn.text().lower() == "window edit":
            self.stacked_layout.setCurrentIndex(2)
            
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
         
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SlackWindow()
    sys.exit(app.exec())
        