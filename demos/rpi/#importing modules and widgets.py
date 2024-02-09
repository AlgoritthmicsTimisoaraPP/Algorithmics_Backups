#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit
 
#declaring constants
win_width, win_height = 200, 300
win_x, win_y = 200, 200
txt_title = "Magic calculator"
txt_line = "Entry field"
 
class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()
 
        #determines how the window will look (text, size, location)
        self.set_appear()
 
        # start:
        self.show()
 
    def initUI(self):
        ''' creates graphical elements '''
        self.lable_finish = QLabel()
        self.button_scad = QPushButton("-", self)
        self.button_add = QPushButton("+", self)
        self.button_mult = QPushButton("*", self)
        self.button_div = QPushButton("/", self)
        self.button_equal = QPushButton("=", self)
        self.button_dot = QPushButton(".", self)
        self.button_negative = QPushButton("*-1", self)
        self.button_C = QPushButton("C", self)
        self.button_CE= QPushButton("CE", self)
        self.button_remove = QPushButton("←", self)

        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)
        self.button_0 = QPushButton("0", self)

        self.layout_line = QVBoxLayout()


        coloum1_layout = QVBoxLayout()
        coloum2_layout = QVBoxLayout()
        coloum3_layout = QVBoxLayout()
        coloum4_layout = QVBoxLayout()
        

        coloum1_layout.addWidget(self.button_CE, alignment = Qt.AlignCenter)
        coloum1_layout.addWidget(self.button_7, alignment = Qt.AlignCenter)
        coloum1_layout.addWidget(self.button_4, alignment = Qt.AlignCenter)
        coloum1_layout.addWidget(self.button_1, alignment = Qt.AlignCenter)
        coloum1_layout.addWidget(self.button_negative, alignment = Qt.AlignCenter)

        coloum2_layout.addWidget(self.button_C, alignment = Qt.AlignCenter)
        coloum2_layout.addWidget(self.button_8, alignment = Qt.AlignCenter )
        coloum2_layout.addWidget(self.button_5, alignment = Qt.AlignCenter )
        coloum2_layout.addWidget(self.button_2, alignment = Qt.AlignCenter )
        coloum2_layout.addWidget(self.button_0, alignment = Qt.AlignCenter )

        coloum3_layout.addWidget(self.button_remove, alignment = Qt.AlignCenter)
        coloum3_layout.addWidget(self.button_9, alignment = Qt.AlignCenter)
        coloum3_layout.addWidget(self.button_6, alignment = Qt.AlignCenter)
        coloum3_layout.addWidget(self.button_3, alignment = Qt.AlignCenter)
        coloum3_layout.addWidget(self.button_dot, alignment = Qt.AlignCenter)
        
        coloum4_layout.addWidget(self.button_div, alignment = Qt.AlignCenter)
        coloum4_layout.addWidget(self.button_mult, alignment = Qt.AlignCenter)
        coloum4_layout.addWidget(self.button_scad, alignment = Qt.AlignCenter)
        coloum4_layout.addWidget(self.button_add, alignment = Qt.AlignCenter)
        coloum4_layout.addWidget(self.button_equal, alignment = Qt.AlignCenter)

        coloum1.setLayout(coloum1_layout)
        coloum2.setLayout(coloum2_layout)
        coloum3.setLayout(coloum3_layout)
        coloum4.setLayout(coloum4_layout)


        self.general_layout = QHBoxLayout()

        
        self.general_layout.addWidget(coloum1)
        self.general_layout.addWidget(coloum2)
        self.general_layout.addWidget(coloum3)
        self.general_layout.addWidget(coloum4)


        self.setLayout(self.general_layout)
 

 
 
    def connects(self):
        # Nu need for the buttons to do something in this exercise/nothing to add here 
        pass
 
    ''' determines how the window will look (text, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()