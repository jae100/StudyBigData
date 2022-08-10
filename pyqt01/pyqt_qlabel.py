import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



# 클래스 OOP
class qTemplate(QWidget):
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    # 화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png')) # 윈도우아이콘 지정
        self.setGeometry(300, 200, 500, 200)#화면의 위치 크기 조정
        self.setWindowTitle('QTemplate!!!') # 화면의 제목
        self.text = 'What a wonderful world~'# 글자 작성은 여러함수가 있다
        self.show()
    
    def addControls(self) -> None:
        self.setWindowIcon()
        label1 = QLabel('', self)
        label2 = QLabel('', self)
        label1.setStyleSheet(
            ('border-width: 3px;'
            'border-style:solid;'
            'border-color: blue;'
            'image: url(./pyqt01/image/image1.png)')
        )
        label2.setStyleSheet(
            ('border-width: 3px;'
            'border-style: dot-dot-dash;'
            'border-color: blue;'
            'image: url(./pyqt01/image/image2.png)')
        )

        box = QHBoxLayout() #QVBoxLayout 세로로 레이아웃 정의,QHBoxLayout 가로로 레이아웃 정의
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()