from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        #calling a constructor of the parent class
        super().__init__(parent=parent, flags=flags)

        # creating and customizing the graphical elements:
        self.initUI()

        #connects the elements
        self.connects()

        #determines how the window will look (text, size, location)
        self.set_appear()

        # start:
        self.show()




#creating a main function for the project
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
#launching the project

if __name__ == "__main__":
    main()
