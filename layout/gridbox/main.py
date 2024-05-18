import sys

from PyQt6.QtWidgets import (QApplication, QWidget
,QPushButton, QMessageBox, QTextEdit, QLabel,QLineEdit, QGridLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.first_value = ''
        self.second_value = ''
        self.operator = ''
        self.pointer_flag = '1'
        self.after_equal = False
        self.after_operator = False
        
    def initUI(self):
        self.setWindowTitle("Calculadora")
        self.setGeometry(300,300,600,400)
        self.generar_contenido()
        self.show()
        
    def generar_contenido(self):
        self.screen = QTextEdit()
        self.screen.setDisabled(True)
        btn1 = QPushButton ("1")
        btn2 = QPushButton ("2")
        btn3 = QPushButton ("3")
        btn4 = QPushButton ("4")
        btn5 = QPushButton ("5")
        btn6 = QPushButton ("6")
        btn7 = QPushButton ("7")
        btn8 = QPushButton ("8")
        btn9 = QPushButton ("9")
        btn10 = QPushButton ("00")
        btn11 = QPushButton ("0")
        btn12 = QPushButton (".")
        btn13 = QPushButton ("+")
        btn14 = QPushButton ("-")
        btn15 = QPushButton ("*")
        btn16 = QPushButton ("/")
        btn17 = QPushButton ("=")
        btn18 = QPushButton ("⌫")
        btn19 = QPushButton ("AC")
        btn20 = QPushButton ("x^")
        btn21 = QPushButton ("x!")
        btn22 = QPushButton ("π")
        btn23 = QPushButton ("√")
        btn24 = QPushButton ("1/x")
        btn25 = QPushButton ("sin")
        btn26 = QPushButton ("cos")
        btn27 = QPushButton ("tan")
        btn28 = QPushButton ("ln")
        btn29 = QPushButton ("log")
        btn30 = QPushButton ("x^2")
        
        
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.screen,0,0,2,4)
        self.main_grid.addWidget(btn23,2,0,1,1)
        self.main_grid.addWidget(btn30,2,1,1,1)
        self.main_grid.addWidget(btn25,2,2,1,1)
        self.main_grid.addWidget(btn26,2,3,1,1)
        self.main_grid.addWidget(btn27,2,4,1,1)
        
        self.main_grid.addWidget(btn28,3,0,1,1)
        self.main_grid.addWidget(btn29,3,1,1,1)
        self.main_grid.addWidget(btn19,3,2,1,1)
        self.main_grid.addWidget(btn18,3,3,1,1)
        self.main_grid.addWidget(btn16,3,4,1,1)
        
        self.main_grid.addWidget(btn24,4,0,1,1)
        self.main_grid.addWidget(btn7,4,1,1,1)
        self.main_grid.addWidget(btn8,4,2,1,1)
        self.main_grid.addWidget(btn9,4,3,1,1)
        self.main_grid.addWidget(btn15,4,4,1,1)
        
        self.main_grid.addWidget(btn21,5,0,1,1)
        self.main_grid.addWidget(btn4,5,1,1,1)
        self.main_grid.addWidget(btn5,5,2,1,1)
        self.main_grid.addWidget(btn6,5,3,1,1)
        self.main_grid.addWidget(btn14,5,4,1,1)
        
        self.main_grid.addWidget(btn22,6,0,1,1)
        self.main_grid.addWidget(btn1,6,1,1,1)
        self.main_grid.addWidget(btn2,6,2,1,1)
        self.main_grid.addWidget(btn3,6,3,1,1)
        self.main_grid.addWidget(btn13,6,4,1,1)
        
        self.main_grid.addWidget(btn20,7,0,1,1)
        self.main_grid.addWidget(btn11,7,1,1,1)
        self.main_grid.addWidget(btn10,7,2,1,1)
        self.main_grid.addWidget(btn12,7,3,1,1)
        self.main_grid.addWidget(btn17,7,4,1,1)
        
        self.setLayout(self.main_grid)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        