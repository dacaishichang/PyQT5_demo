import sys
from PyQt5.QtWidgets import *

class CenterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('哈哈哈')
        #显示窗口
        self.show()
    #让窗口居中
    def center(self):
        #得到窗口对象
        desk=app.desktop()
        self.move((desk.width()-self.width())/2,(desk.height()-self.height())/2)

app=QApplication(sys.argv)
w=CenterWidget()
sys.exit(app.exec_())