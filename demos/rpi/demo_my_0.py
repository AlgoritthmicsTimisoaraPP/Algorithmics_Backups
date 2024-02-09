import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Application')

        layout = QVBoxLayout(self)

        self.label = QLabel('Enter your name:', self)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.button = QPushButton('Click me!', self)
        self.button.clicked.connect(self.show_message)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_message(self):
        name = self.input_field.text()
        ani = 19
        if name:
            message = f"Hello, {name}, ceau {ani}!"
        else:
            message = "Hello, stranger!"
        QMessageBox.information(self, 'Message', message)
    # def exec_(se):
    #     print(exit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    # sys.exit(window.exec_())
