#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
 
from PyQt5 import *
#declaring constants
win_width, win_height = 250, 500
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "0"

class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        # self.connects()
 
        #determines how the window will look (text, size, location)
        # self.set_appear()
 
        # start:
        self.show()
 
    def initUI(self):
        ''' creates graphical elements '''
        self.setFixedWidth(win_width)
        self.setFixedHeight(win_height)
        qestion = QLabel("Question:")
        btn_add = QPushButton("+", self)
        btn_scad = QPushButton("-", self)
        btn_div = QPushButton("/", self)
        btn_mult = QPushButton("*", self)
        btn_1 = QPushButton("1", self)
        btn_2 = QPushButton("2", self)
        btn_3 = QPushButton("3", self)
        btn_4 = QPushButton("4", self)
        btn_5 = QPushButton("5", self)
        btn_6 = QPushButton("6", self)        
        btn_7 = QPushButton("7", self)
        btn_8 = QPushButton("8", self)
        btn_8.resize(200,200)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(btn_8)
        self.main_layout.addWidget(btn_7)
        self.setLayout(self.main_layout)

 
 
    
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()