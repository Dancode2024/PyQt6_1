import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.screen = QTextEdit()
        self.screen.setReadOnly(True)
        layout.addWidget(self.screen)

        btn20 = QPushButton("x^y")
        btn21 = QPushButton("x!")
        btn22 = QPushButton("π")
        btn23 = QPushButton("√")
        btn24 = QPushButton("1/x")
        btn25 = QPushButton("sin")
        btn26 = QPushButton("cos")
        btn27 = QPushButton("tan")
        btn28 = QPushButton("ln")
        btn29 = QPushButton("log")
        btn30 = QPushButton("x^2")

        buttons = [btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30]
        functions = [self.power, self.factorial, self.pi, self.sqrt, self.inverse, self.sine, self.cosine, self.tangent, self.ln, self.log10, self.square]

        for button, function in zip(buttons, functions):
            layout.addWidget(button)
            button.clicked.connect(function)

        self.setLayout(layout)
        self.setWindowTitle('Calculadora')
        self.show()

    def get_input(self):
        text = self.screen.toPlainText()
        return text.split()[-1] if text else ""

    def append_result(self, result):
        self.screen.setText(self.screen.toPlainText() + f"\n{result}\n")

    def power(self):
        base = float(self.get_input())
        exponent = float(self.get_input())
        result = math.pow(base, exponent)
        self.append_result(result)

    def factorial(self):
        num = int(self.get_input())
        result = math.factorial(num)
        self.append_result(result)

    def pi(self):
        result = math.pi
        self.append_result(result)

    def sqrt(self):
        num = float(self.get_input())
        result = math.sqrt(num)
        self.append_result(result)

    def inverse(self):
        num = float(self.get_input())
        result = 1 / num
        self.append_result(result)

    def sine(self):
        num = float(self.get_input())
        result = math.sin(math.radians(num))
        self.append_result(result)

    def cosine(self):
        num = float(self.get_input())
        result = math.cos(math.radians(num))
        self.append_result(result)

    def tangent(self):
        num = float(self.get_input())
        result = math.tan(math.radians(num))
        self.append_result(result)

    def ln(self):
        num = float(self.get_input())
        result = math.log(num)
        self.append_result(result)

    def log10(self):
        num = float(self.get_input())
        result = math.log10(num)
        self.append_result(result)

    def square(self):
        num = float(self.get_input())
        result = math.pow(num, 2)
        self.append_result(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec())
