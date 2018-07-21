import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCalendarWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QDate

class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #垂直布局
        vbox=QVBoxLayout(self)
        #建立日历
        cal=QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        #加入日历
        vbox.addWidget(cal)
        date=cal.selectedDate()

        self.lbl=QLabel(self)
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        self.setGeometry(300,300,350,350)

        self.setWindowTitle('calendar控件')
        self.show()
    def showDate(self,date):
        self.lbl.setText(date.toString())

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=CalendarWidget()
    sys.exit(app.exec_())