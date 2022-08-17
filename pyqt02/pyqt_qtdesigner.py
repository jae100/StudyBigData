import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui',self) # qtdesign에서 만든 파일을 불러와 로드 시키면 코딩을 하지 않아도 쉽게 화면GUI를 만들수 있다
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self)-> None:
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결

    def btn1_clicked(self):
        self.label.setText('메시지 : btn1 버튼 클릭!!!')
        QMessageBox.information(self,'signal','btn1_clicked!!') # information은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.

    def btn1_clicked(self):
        QMessageBox.information(self,'signal','btn1_clicked!!') # information은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.
        # QMessageBox.warning(self,'signal','btn1_clicked!!') # warning은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.
        # QMessageBox.critical(self,'signal','btn1_clicked!!') # critical은 알림창이 나올때 어떤 그림이 나오는지 정하는 것.


if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

