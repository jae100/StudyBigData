import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 500, 200)
        self.setWindowTitle('QPushbutton')
        self.show()

    def addControls(self)-> None:
        btn1 = QPushButton('Click', self)
        btn1.setGeometry(10, 10, 120, 40)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

