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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Formulario")
        self.setFixedSize( 350, 200)
        self.setWindowTitle("Formulario")
        self.generation_form()
        self.show()
        
    def generation_form(self):
        titulo = QLabel("Formulario") # Asignacion de titulo
        titulo.setFont(QFont("Arial",18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)# centramos el contenido
        
        self.name_edit = QLineEdit()
        #self.name_edit.resize(180,24)
        self.name_edit.setPlaceholderText("Nombre")
        
        self.lastname_edit = QLineEdit()
        self.lastname_edit.setPlaceholderText("Apellido")
        
        self.options_edit = QComboBox()
        self.options_edit.addItems([" ","Womens","Man"])
        
        self.fecha_nac = QDateEdit()
        self.fecha_nac.setDisplayFormat("yyyy-MM-dd")
        self.fecha_nac.setMaximumDate(QDate.currentDate())
        self.fecha_nac.setCalendarPopup(True)
        self.fecha_nac.setDate(QDate.currentDate())                             
        
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("9196599822")
        
        submit_buttom = QPushButton()
        submit_buttom.setText("Submit")
        submit_buttom.clicked.connect(self.show_info)
        
        first_h_box = QHBoxLayout()
        first_h_box.addWidget(self.name_edit)
        first_h_box.addWidget(self.lastname_edit)
        
        main_form  = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Name: ",first_h_box)
        main_form.addRow("Genero: ", self.options_edit)
        main_form.addRow("Fecha: ", self.fecha_nac)
        main_form.addRow("Phone: ", self.phone)
        main_form.addRow(submit_buttom)
        
        self.setLayout(main_form)
        
    def show_info(self):
        name = self.name_edit.text()
        lastname = self.lastname_edit.text()
        genero = self.options_edit.currentText()
        fecha = self.fecha_nac.text()
        phone = self.phone.text()
        
        message = f"Name: {name}\nLastname: {lastname}\n Genero: {genero}\nFecha: {fecha}\nPhone: {phone}"
        QMessageBox.information(self,"Informacion",message)
        

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        