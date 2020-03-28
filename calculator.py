import sys # For access to command line args
from PySide2.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()

# Windows are hidden by default
window.show()

app.exec_()