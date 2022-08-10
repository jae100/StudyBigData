import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt



# 클래스 OOP
class qTemplate(QWidget):
    # 생성자, 생성자는 기본적으로 return값이 없다. 그래서 None
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    # 화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.setGeometry(300, 200, 500, 200)#화면의 위치 크기 조정
        self.setWindowTitle('QTemplate!!!') # 화면의 제목
        self.text = 'What a wonderful world~'# 글자 작성은 여러함수가 있다
        self.show()

    def paintEvent(self, event) -> None:# 화면을 이동하면 화면안의 내용도 같이 옮기는 역할을 한다,QWidget의 기본 함수
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    def drawText(self, event, paint):# 화면안의 글자 입력
        paint.setPen(QColor(255,255,250))
        paint.setFont(QFont('NanumGothic',20))
        paint.drawText(105, 100, 'HELL WORLD~')#drawText는 Qpaint의 내장함수
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)# AlignCenter 글자의 위치를 화면의 정중아에 위치 시킨다. self.text의 글자를 불러옴

if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()