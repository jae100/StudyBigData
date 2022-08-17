import sys
from unittest import TextTestRunner
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time

# UI 스레드와 작업스레드 분리
class Worker(QThread):
        #QTread는 UI를 그릴 권한이없다
        valChangeSignal = pyqtSignal(int)
        def __init__(self,parent) -> None:
            super().__init__(parent)
            self.parent = parent
            self.working = True # 클래스 내부변수 working을 지정

        def run(self):
            while self.working:
                for i in range(0, 100):
                    print(f'출력 : {i}')
                    # self.pgbTask.setValue(i)
                    # self.txblog.append(f'출력>{i}') # 화면 그리는 작업
                    self.valChangeSignal.emit(i) # UI스레트야 화면은 너가 그려줘~
                    time.sleep(0.0001) # 1micro sec



# 클래스 OOP
class qTemplate(QWidget):
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    # 대신 통신을 통해서 UI스레드가 그림을 그릴 수있도록 통신수행
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/navernews.ui',self)
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self)-> None:
        pass



if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

