import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox

class MessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('哈哈哈')
        #显示窗口
        self.show()
    def closeEvent(self,event):
        #显示询问对话框，捕获消息
        reply=QMessageBox.question(self,'消息','你真的要退出么？',
                                   QMessageBox.Yes|QMessageBox.No)
        #接受退出
        if reply==QMessageBox.Yes:
            event.accept()
        #忽略消息
        else:
            event.ignore()

app=QApplication(sys.argv)
mb=MessageBox()
sys.exit(app.exec_())