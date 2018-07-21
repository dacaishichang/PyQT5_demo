import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

app=QApplication(sys.argv)
w=QWidget()
#设置窗口
w.setGeometry(300,300,300,300)
#设置标题
w.setWindowTitle('我的窗口')
#设置Icon图像
app.setWindowIcon(QIcon('./hmbb.jpg'))
#显示
w.show()
#退出
sys.exit(app.exec_())