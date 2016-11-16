import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

# two different window classes to make sure I know exactly what's happening
# and couldn't find out how to put them in one - is that even possible?
class SolvedWindow(QWidget):
    def __init__(self):
        super(SolvedWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('CONGRATULATIONS!')
        # no button or text needed; everything's in the png
        filepath = "media/solved.png"
        self.mypixmap = QPixmap(filepath)
        self.myimg = QLabel(self)
        self.myimg.setPixmap(self.mypixmap)

        pixrect = self.mypixmap.rect()
        self.setGeometry(10, 10, pixrect.width(), pixrect.height() + 50)
        self.show()

class UnsolvedWindow(QWidget):
    def __init__(self):
        super(UnsolvedWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('YOU ARE A SHAME!')
        # no button or text needed; everything's in the png
        filepath = "media/unsolved.png"
        self.mypixmap = QPixmap(filepath)
        self.myimg = QLabel(self)
        self.myimg.setPixmap(self.mypixmap)

        pixrect = self.mypixmap.rect()
        self.setGeometry(10, 10, pixrect.width(), pixrect.height() + 50)
        self.show()

# limiting line length to 80 characters because ... style, that's why.
