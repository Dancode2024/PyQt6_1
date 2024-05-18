import sys
import math
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
        
        btn1.clicked.connect(self.ingresar_datos)
        btn2.clicked.connect(self.ingresar_datos)
        btn3.clicked.connect(self.ingresar_datos)
        btn4.clicked.connect(self.ingresar_datos)
        btn5.clicked.connect(self.ingresar_datos)
        btn6.clicked.connect(self.ingresar_datos)
        btn7.clicked.connect(self.ingresar_datos)
        btn8.clicked.connect(self.ingresar_datos)
        btn9.clicked.connect(self.ingresar_datos)
        btn10.clicked.connect(self.ingresar_datos)
        btn11.clicked.connect(self.ingresar_datos)
        btn12.clicked.connect(self.ingresar_datos)
        btn13.clicked.connect(self.ingresar_operator)
        btn14.clicked.connect(self.ingresar_operator)
        btn15.clicked.connect(self.ingresar_operator)
        btn16.clicked.connect(self.ingresar_operator)
        btn17.clicked.connect(self.calculator_operation)
        btn18.clicked.connect(self.delete_parcial)
        btn19.clicked.connect(self.delete_all)
        btn20.clicked.connect(self.ingresar_operatior)
        btn21.clicked.connect(self.ingresar_operatior)
        btn22.clicked.connect(self.ingresar_operatior)
        btn23.clicked.connect(self.ingresar_operatior)
        btn24.clicked.connect(self.ingresar_operatior)
        btn25.clicked.connect(self.ingresar_operatior)
        btn26.clicked.connect(self.ingresar_operatior)
        btn27.clicked.connect(self.ingresar_operatior)
        btn28.clicked.connect(self.ingresar_operatior)
        btn29.clicked.connect(self.ingresar_operatior)
        btn30.clicked.connect(self.ingresar_operatior)
        
        self.setLayout(self.main_grid)
        
    def ingresar_datos(self):
        button_text = self.sender().text()
        if self.pointer_flag == 'A':  # Verificar si se ingresó una operación especial como raíz cuadrada
            self.first_value = float(button_text)  # Convertir el número a float
            self.screen.setText(str(self.first_value))  # Mostrar el número en la pantalla
            self.pointer_flag = '1'  # Establecer el estado para el siguiente número de operación
        elif self.pointer_flag == '1':  # Si se está ingresando el primer número
            if self.operator == '√':  # Si la operación actual es raíz cuadrada
                self.second_value = button_text  # Almacenar el número como segundo valor
                self.pointer_flag = '2'  # Cambiar al modo de entrada del segundo número
                self.screen.setText(self.screen.toPlainText() + button_text)  # Mostrar el número en la pantalla
            else:
                self.first_value += button_text  # Agregar el dígito al primer valor
                self.screen.setText(self.first_value)  # Mostrar el primer valor en la pantalla
        else:  # Si se está ingresando el segundo número
            self.second_value += button_text  # Agregar el dígito al segundo valor
            self.screen.setText(self.screen.toPlainText() + button_text)  # Mostrar el segundo valor en la pantalla 
            
    def ingresar_operatior(self):
        operation = self.sender().text()
        if operation == 'x^' and operation == 'x!' and operation == 'π' and operation == '√' and operation == '1/x' and operation == 'sin' and operation == 'cos' and operation == 'tan' and operation == 'ln' and operation == 'log' and operation == 'x^2':  # Si se presiona el botón de raíz cuadrada
            self.operator = operation  # Establecer el operador como raíz cuadrada
            self.screen.setText(self.screen.toPlainText() + operation)
            self.pointer_flag = '1'  # Cambiar al modo de entrada del primer número
        else:  # Si se presiona cualquier otro botón de operación
            self.operator = operation
            self.screen.setText(self.screen.toPlainText() + operation)
            self.pointer_flag = '2'  # Cambiar al modo de entrada del segundo número (si es necesario)
            self.after_operator = True  # Indicar que se ha ingresado un operador
            
    def ingresar_operator(self):
        operator_button = self.sender().text()
        self.operator = operator_button
        self.screen.setText(self.screen.toPlainText()+operator_button)
        self.pointer_flag = '2'
        self.after_equal = False
        self.after_operator = True 
        
    def calculator_operation(self):
        try:
            if self.operator:
                
                first_num = float(self.first_value) 
                second_num = float(self.second_value) if self.second_value else None
                result = 0
            
            if self.operator == '+':
                result = first_num + second_num
            elif self.operator == '-':
                result = first_num - second_num
            elif self.operator == '*':
                result = first_num * second_num
            elif self.operator == '/':
                result = first_num / second_num
            elif self.operator == 'x^':
                result = first_num ** second_num
            elif self.operator == 'x!':
                result = math.factorial(first_num)
            elif self.operator == '√':
                result = math.sqrt(first_num)
            elif self.operator == '1/x':
                result = 1 / first_num
            elif self.operator == 'sin':
                result = math.sin(math.radians(first_num))
            elif self.operator == 'cos':
                result = math.cos(math.radians(first_num))
            elif self.operator == 'tan':
                result = math.tan(math.radians(first_num))
            elif self.operator == 'ln':
                result = math.log(first_num)
            elif self.operator == 'log':
                result = math.log10(first_num)
            elif self.operator == 'π':
                result = math.pi
            
            self.screen.setText(str(result))
            self.first_value = str(result)
            
        except Exception as e:
            self.screen.setText(f"Error: {e}")

    
    def delete_parcial(self):
        if self.after_equal:
            self.delete_all()
            
        if self.pointer_flag == '1':
            self.first_value = self.first_value[:-1]
            self.screen.setText(self.first_value)
            self.operator = ''
                    
        else:
            self.second_value = self.second_value[:-1]
            self.screen.setText(self.screen.toPlainText()+self.second_value)
    
    def delete_all(self):
        self.first_value = ''
        self.second_value = ''
        self.operator = ''
        self.pointer_flag = '1'
        self.after_equal = False
        self.after_operator = False
        self.screen.setText('')
            
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        