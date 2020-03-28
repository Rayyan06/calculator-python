import sys # For access to command line args
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from random import *

class Calculator(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_UI()



    def init_UI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Calculator")

        self.label = QLabel("Calculator")

        self.label.setAlignment(Qt.AlignCenter)

        self.init_buttons()

        
    def init_buttons(self):

        self.equalButton = QPushButton(self)
        self.addButton = QPushButton(self)
        self.subtractButton = QPushButton(self)
        self.multiplyButton = QPushButton(self)
        self.divideButton = QPushButton(self)
        self.clearButton = QPushButton(self)
        self.deleteButton = QPushButton(self)
        self.number_buttons = []
        for i in range(0, 10):

            self.number_buttons.append(QPushButton(self))

            self.number_buttons[i].setText(str(i))
            #  SIGNAL

        # TODO: Fix this mess; DRY (Don't Repeat Yourself); For loop not working, fix it!
        self.number_buttons[0].clicked.connect(lambda: self.pressNumber(0))
        self.number_buttons[1].clicked.connect(lambda: self.pressNumber(1))
        self.number_buttons[2].clicked.connect(lambda: self.pressNumber(2))
        self.number_buttons[3].clicked.connect(lambda: self.pressNumber(3))
        self.number_buttons[4].clicked.connect(lambda: self.pressNumber(4))
        self.number_buttons[5].clicked.connect(lambda: self.pressNumber(5))
        self.number_buttons[6].clicked.connect(lambda: self.pressNumber(6))
        self.number_buttons[7].clicked.connect(lambda: self.pressNumber(7))
        self.number_buttons[8].clicked.connect(lambda: self.pressNumber(8))
        self.number_buttons[9].clicked.connect(lambda: self.pressNumber(9))


        # Move The Buttons to their correct positions

        self.number_buttons[0].move(100, 200)
        self.number_buttons[1].move(180, 100)
        self.number_buttons[2].move(80, 100)
        self.number_buttons[3].move(170, 100)
        self.number_buttons[4].move(60, 100)
        self.number_buttons[5].move(150, 200)
        self.number_buttons[6].move(40, 100)
        self.number_buttons[7].move(30, 100)
        self.number_buttons[8].move(20, 100)
        self.number_buttons[9].move(10, 100)
    # SLOT This accepts a number; from a button; and prints it
    def pressNumber(self, i):
        print(i, end="")

def window():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec_()

if __name__=="__main__":
    window()