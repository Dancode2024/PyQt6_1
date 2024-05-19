import sys
import math
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QTextEdit, QGridLayout)

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
        self.setGeometry(300, 300, 600, 400)
        self.generar_contenido()
        self.show()
        
    def generar_contenido(self):
        self.screen = QTextEdit()
        self.screen.setDisabled(True)
        
        btn_text = [
            ("1", 6, 1), ("2", 6, 2), ("3", 6, 3), ("4", 5, 1), ("5", 5, 2),
            ("6", 5, 3), ("7", 4, 1), ("8", 4, 2), ("9", 4, 3), ("0", 7, 1),
            ("00", 7, 2), (".", 7, 3), ("+", 6, 4), ("-", 5, 4), ("*", 4, 4),
            ("/", 3, 4), ("=", 7, 4), ("⌫", 3, 3), ("AC", 3, 2), ("x^", 7, 0),
            ("x!", 5, 0), ("π", 6, 0), ("√", 2, 0), ("1/x", 4, 0), ("sin", 2, 2),
            ("cos", 2, 3), ("tan", 2, 4), ("ln", 3, 0), ("log", 3, 1), ("x^2", 2, 1)
        ]
        
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.screen, 0, 0, 2, 5)
        
        for (text, row, col) in btn_text:
            button = QPushButton(text)
            self.main_grid.addWidget(button, row, col)
            if text in "0123456789.":
                button.clicked.connect(self.ingresar_datos)
            elif text == "=":
                button.clicked.connect(self.calculator_operation)
            elif text == "AC":
                button.clicked.connect(self.delete_all)
            elif text == "⌫":
                button.clicked.connect(self.delete_parcial)
            elif text == "√":
                button.clicked.connect(self.sqrt)
            elif text == "x^2":
                button.clicked.connect(self.square)
            else:
                button.clicked.connect(self.ingresar_operator)
        
        self.setLayout(self.main_grid)
  
    def sqrt(self):
        try:
            value = float(self.first_value)
            result = math.sqrt(value)
            self.screen.setText(str(result))
            self.first_value = str(result)
            self.pointer_flag = '1'
        except ValueError:
            self.screen.setText("Error")
            self.first_value = ''
            self.pointer_flag = '1'
    
    def square(self):
        try:
            value = float(self.first_value)
            result = value ** 2
            self.screen.setText(str(result))
            self.first_value = str(result)
            self.pointer_flag = '1'
        except ValueError:
            self.screen.setText("Error")
            self.first_value = ''
            self.pointer_flag = '1'
    
    def ingresar_datos(self):
        button_text = self.sender().text()
              
        if self.after_equal:
            self.first_value = button_text
            self.second_value = ''
            self.operator = ''
            self.screen.setText(self.first_value)
            self.after_equal = False
            self.pointer_flag = '1'
        else:
            if self.after_operator:
                self.second_value += button_text
                self.screen.setText(self.screen.toPlainText() + button_text)
            else:
                if self.pointer_flag == '1':
                    self.first_value += button_text
                    self.screen.setText(self.first_value)
                else:
                    self.second_value += button_text
                    self.screen.setText(self.screen.toPlainText() + button_text)

        self.after_operator = False
    
    def ingresar_operator(self):
        operator_button = self.sender().text()
        if self.after_operator:
            self.calculator_operation()
            self.first_value = self.screen.toPlainText()
            self.second_value = ''
            self.operator = operator_button
            self.screen.setText(self.first_value + ' ' + self.operator + ' ')
        else:
            self.operator = operator_button
            self.screen.setText(self.screen.toPlainText() + ' ' + self.operator + ' ')
        
        self.pointer_flag = '2'
        self.after_operator = True 
        self.after_equal = False
    
    def calculator_operation(self):
        result = 0
        try:
            first_num = float(self.first_value)
            second_num = float(self.second_value) if self.second_value else None
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
                result = math.factorial(int(first_num))
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
            self.second_value = ''
            self.pointer_flag = '1'
            self.after_equal = True
            self.after_operator = False
        except Exception as e:
            self.screen.setText("Error: Entrada invalida")
            self.first_value = ''
            self.second_value = ''
            self.operator = ''
            self.pointer_flag = '1'
            self.after_equal = False
            self.after_operator = False
       
    def delete_all(self):
        self.first_value = ''
        self.second_value = ''
        self.operator = ''
        self.pointer_flag = '1'
        self.after_equal = False
        self.after_operator = False
        self.screen.setText('')
    
    def delete_parcial(self):
        if self.after_equal:
            self.delete_all()
        elif self.pointer_flag == '1':
            self.first_value = self.first_value[:-1]
            self.screen.setText(self.first_value)
        else:
            self.second_value = self.second_value[:-1]
            self.screen.setText(self.screen.toPlainText()[:-1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
