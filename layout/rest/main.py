import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QLineEdit,QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(100,100,400,150)
        self.generate_login()
        self.show()
        
    def generate_login(self):
        message = QLabel("Ingrese sus datos...")
        
        user_label = QLabel("User: ")
        user_label.setFixedWidth(60)
        self.user_input= QLineEdit()
        
        last_name = QLabel("Last user: ")
        last_name.setFixedWidth(60)
        self.last_name_input = QLineEdit()
        
        age = QLabel("Age: ")
        age.setFixedWidth(60)
        self.age_input = QLineEdit()
        
        address = QLabel("Address: ")
        address.setFixedWidth(60)
        self.address_input = QLineEdit()
        
        email = QLabel("email: ")
        email.setFixedWidth(60)
        self.email_input = QLineEdit()
        
        phone = QLabel("Phone: ")
        phone.setFixedWidth(60)
        self.phone_input = QLineEdit()
        
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_data)
        
        vertical_layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        
        h_layout_1.addWidget(user_label)
        h_layout_1.addWidget(self.user_input)
        h_layout_1.addWidget(last_name)
        h_layout_1.addWidget(self.last_name_input)
        
        h_layout_2.addWidget(age)
        h_layout_2.addWidget(self.age_input)
        h_layout_2.addWidget(address)
        h_layout_2.addWidget(self.address_input)
        
        h_layout_3.addWidget(email)
        h_layout_3.addWidget(self.email_input)
        h_layout_3.addWidget(phone)
        h_layout_3.addWidget(self.phone_input)
        
        vertical_layout.addWidget(message)
        vertical_layout.addLayout(h_layout_1)
        vertical_layout.addLayout(h_layout_2)
        vertical_layout.addLayout(h_layout_3)
        vertical_layout.addWidget(send_button)
        
        self.setLayout(vertical_layout)
        
    def send_data(self):
        QMessageBox.information(self, "Exito", 
        'Usuario creado exitosamente',
        QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.Ok)
        
          
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    