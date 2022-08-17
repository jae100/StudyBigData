import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/ttask.ui',self)
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self)-> None:
        self.btnStart.clicked.connect(self.btn1_clicked) # 시그널 연결

    def btn1_clicked(self):
        self. txblog.append('실행!!')
        self.pgbTask.setRange(0,99) #range를 99이상으로 하면 응답없음 나옴
        for i in range(0, 100):
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txblog.append(f'출력>{i}')


if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

