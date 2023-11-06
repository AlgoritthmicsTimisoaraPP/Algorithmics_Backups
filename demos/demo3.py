#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
 
#declaring constants
win_width, win_height = 250, 500
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "0"

class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
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

        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()
        v4 = QVBoxLayout()

        v1.addWidget(btn_7)
        v1.addWidget(btn_4)
        v1.addWidget(btn_1)

        v2.addWidget(btn_8)
        v2.addWidget(btn_5)
        v2.addWidget(btn_2)

        w1 = QWidget()
        w2 = QWidget()


        w1.setLayout(v1)
        w2.setLayout(v2)

        
 
        self.layout_line = QHBoxLayout()
        self.layout_line.addWidget(w1,  alignment = Qt.AlignCenter)
        self.layout_line.addWidget(w2,  alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)
 
 
    
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()