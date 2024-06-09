from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.initUI()

    def initUI(self):
        # Create layout
        main_layout = QVBoxLayout()

        # Create display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 20px;")
        main_layout.addWidget(self.display)

        # Create buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Add buttons to layout
        for row in buttons:
            row_layout = QHBoxLayout()
            for btn_text in row:
                button = QPushButton(btn_text)
                button.setFixedSize(60, 60)
                button.setStyleSheet("font-size: 18px;")
                button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)
            main_layout.addLayout(row_layout)

        self.setLayout(main_layout)

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif button_text == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + button_text)
