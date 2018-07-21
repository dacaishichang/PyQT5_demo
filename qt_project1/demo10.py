import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QLabel
from PyQt5.QtGui import QPixmap
class PixMap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #布局创建
        hbox=QHBoxLayout(self)
        pixmap=QPixmap('hmbb.jpg')
        #嵌在里面
        lbl=QLabel(self)
        #设置图片
        lbl.setPixmap(pixmap)
        #布局加入
        hbox.addWidget(lbl)
        #设置布局
        self.setLayout(hbox)

        self.move(300,200)
        self.setWindowTitle('显示图像')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=PixMap()
    sys.exit(app.exec_())