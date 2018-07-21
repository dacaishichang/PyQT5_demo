import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont

app=QApplication(sys.argv)
w=QWidget()
w.setGeometry(300,300,300,300)
w.setWindowTitle('提示框')
#字体
QToolTip.setFont(QFont('SansSerif',20))
#鼠标移动到这里，显示什么
w.setToolTip('这是一个窗口\n窗口设计者：黄华飞')
#设计按钮，嵌入w内
button=QPushButton('按钮',w)
#标题
button.setToolTip('按钮设计者：黄华飞')
#大小
button.resize(button.sizeHint())
#位置
button.move(50,50)
w.show()
sys.exit(app.exec_())