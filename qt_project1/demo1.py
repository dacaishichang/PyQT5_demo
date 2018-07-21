import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget

app=QApplication(sys.argv)
#创建窗口
w=QWidget()
#设置窗口宽高
w.resize(550,300)
#移动窗口位置
w.move(300,300)
#设置窗口标题
w.setWindowTitle("my first application")
w.show()
sys.exit(app.exec_())



