#Slider滑动模块
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox,QLabel,QSlider
from PyQt5.QtCore import Qt
class Slider(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        slider=QSlider(Qt.Horizontal,self)
        #设置最小最大值
        slider.setMinimum(10)
        slider.setMaximum(500)
        slider.setGeometry(30,40,200,80)
        slider.valueChanged[int].connect(self.changeValue)

        self.label=QLabel(self)
        self.label.setGeometry(300,300,280,170)
        self.setWindowTitle("Qslider控件")

        self.show()
    def changeValue(self,value):
        self.label.setText(str(value))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Slider()
    sys.exit(app.exec_())



