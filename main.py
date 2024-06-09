from PySide6 import QtWidgets
from calculator import Calculator

app = QtWidgets.QApplication([])
calc = Calculator()

calc.show()
app.exec()
