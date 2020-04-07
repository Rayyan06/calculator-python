
'''

Program Structure/PseudoCode


1. Import Libraries

    (A)---  sys
    (B) Pyside  

        (I)---Pyside2.QtWidgets
        (I)---PySide2.QtCore


2. Calculator Class

    (A)--- Initialize UI
        (I)----- Set Window Size
        (II)---- Set window Title
        (III)--- Set Label
        (IV)---- Initialize Buttons--(2B)
    
    (B)--- Initialize Buttons
        (I)--- Create Button Layout---QGridLayout
        (II)-- Create Operator Buttons (+, -, /, *, =, AC, CE)
        (III)--Create Number Buttons (1, 2, 3 ..., 9) With For loop

    





'''


import math
import sys # For access to command line args
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *






class Calculator(QMainWindow):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.output = ""

        self.init_UI()




    def init_UI(self):

        self.setGeometry(200, 200, 300, 300)

        self.setWindowTitle("Calculator")

        self.label = QLabel("Calculator")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.calc_screen = QLabel(self.output)
        self.calc_screen.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.calc_screen.setStyleSheet("QLabel {font: 30pt Helvetica Neue MS}")
        self.init_buttons()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.calc_screen)
        layout.addLayout(self.button_layout)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
    def init_buttons(self):

        self.button_layout = QGridLayout()

        self.equal_button = QPushButton(self)
        self.equal_button.setText("=")

        self.add_button = QPushButton(self)
        self.add_button.setText("+")

        self.subtract_button = QPushButton(self)
        self.subtract_button.setText("-")

        self.multiply_button = QPushButton(self)
        self.multiply_button.setText("*")

        self.divide_button = QPushButton(self)
        self.divide_button.setText("/")

        self.clearButton = QPushButton(self)
        self.clearButton.setText("CE")

        self.deleteButton = QPushButton(self)
        self.deleteButton.setText("AC")

        self.number_buttons = []
        for i in range(0, 10):

            self.number_buttons.append(QPushButton(self))

            self.number_buttons[i].setText(str(i))
            #  SIGNAL

        # TODO: Fix this mess; DRY (Don't Repeat Yourself); For loop not working, fix it!
        self.number_buttons[0].clicked.connect(lambda: self.press(0))
        self.number_buttons[1].clicked.connect(lambda: self.press(1))
        self.number_buttons[2].clicked.connect(lambda: self.press(2))
        self.number_buttons[3].clicked.connect(lambda: self.press(3))
        self.number_buttons[4].clicked.connect(lambda: self.press(4))
        self.number_buttons[5].clicked.connect(lambda: self.press(5))
        self.number_buttons[6].clicked.connect(lambda: self.press(6))
        self.number_buttons[7].clicked.connect(lambda: self.press(7))
        self.number_buttons[8].clicked.connect(lambda: self.press(8))
        self.number_buttons[9].clicked.connect(lambda: self.press(9))

        self.add_button.clicked.connect(lambda:self.press("+"))
        self.subtract_button.clicked.connect(lambda:self.press("-"))
        self.multiply_button.clicked.connect(lambda:self.press("*"))
        self.divide_button.clicked.connect(lambda:self.press("/"))


        self.equal_button.clicked.connect(self.evaluate)
        self.clearButton.clicked.connect(self.clear)


        # Move The Buttons to their correct positions

        '''
        Grid
        
        
        _______________
        |  7  8  9  /  |
        |              |
        |  4  5  6  *  |
        |              |
        |  1  2  3  -  |
        |              |
        |  0     =  +  |
        |______________|

        
        '''

        values    =['7', '8', '9', '/', 'AC',
        '4', '5', '6', '*', 'CE',
        '1', '2', '3', '-', '',
        '0', '', '=', '+', '']

        positions = [[i, j] for i in range(4) for j in range(5)]

        def addButton(button, x, y):
            self.button_layout.addWidget(button, x, y)


            
        addButton(self.number_buttons[0], 3, 0)
        addButton(self.number_buttons[1], 2, 0)
        addButton(self.number_buttons[2], 2, 1)
        addButton(self.number_buttons[3], 2, 2)
        addButton(self.number_buttons[4], 1, 0)
        addButton(self.number_buttons[5], 1, 1)
        addButton(self.number_buttons[6], 1, 2)
        addButton(self.number_buttons[7], 0, 0)
        addButton(self.number_buttons[8], 0, 1)
        addButton(self.number_buttons[9], 0, 2)
        addButton(self.add_button, 3, 3)
        addButton(self.subtract_button,2, 3)
        addButton(self.equal_button, 3, 2)
        addButton(self.multiply_button, 1, 3)
        addButton(self.divide_button, 0, 3)
      
        addButton(self.clearButton, 0, 4)
        addButton(self.deleteButton, 1, 4)


    # SLOT This accepts a number; from a button; and prints it
    def press(self, i):
        print(i, end="")
        self.output = self.output+str(i)
        self.update()


    def evaluate(self):
        self.output = str(eval(self.output))
        self.update()
        print(self.output)


    def update(self):
        self.calc_screen.setText(str(self.output))

    def clear(self):
        self.output =""
        self.update()
def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec_()


if __name__=="__main__":
    main()