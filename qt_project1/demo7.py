import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox
from PyQt5.QtCore import Qt

class CheckBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cb=QCheckBox('请选择我',self)
        cb.move(20,20)
        #信号连接定义的函数
        cb.stateChanged.connect(self.changeTitle)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('还没有选择我')
        self.show()
    def changeTitle(self,state):
        if state==Qt.Checked:
            self.setWindowTitle('已经选择我了')
        else:
            self.setWindowTitle("还没选我")

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=CheckBox()
    sys.exit(app.exec_())