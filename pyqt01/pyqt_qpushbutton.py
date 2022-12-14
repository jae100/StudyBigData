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
        self.label= QLabel('메시지:', self)
        self.label.setGeometry(10, 10, 600, 40)
        self.btn1 = QPushButton('Click', self) # 버튼 문구
        self.btn1.setGeometry(510, 350, 120, 40) # 버튼 위치선정
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결
        self.btn1.clicked.connect(self.btn1_clicked)#시그널 처리

    # event = signal (python)
    def btn1_clicked(self):
        QMessageBox.information(self,'signal','btn1_clicked!!') # information은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.
        # QMessageBox.warning(self,'signal','btn1_clicked!!') # warning은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.
        # QMessageBox.critical(self,'signal','btn1_clicked!!') # critical은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.


if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

