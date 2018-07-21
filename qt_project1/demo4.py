import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtCore import QCoreApplication

app=QApplication(sys.argv)
w=QWidget()
w.setGeometry(300,300,300,300)
w.setWindowTitle('关闭窗口')
button=QPushButton('关闭',w)


button.clicked.connect(QCoreApplication.instance().quit)

button.move(50,50)
w.show()

sys.exit(app.exec_())
