import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QAction, QMenu


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #menuBar-Menu-Action
        menubar=QMenuBar(self)
        fileMenu=menubar.addMenu('文件')
        newAction=QAction('新建',self)

        importMenu=QMenu('导入',self)
        importAction1=QAction('从PDF导入',self)
        importAction2=QAction('从word导入',self)
        #设置Action绑定的函数
        newAction.triggered.connect(self.newaction)
        importAction1.triggered.connect(self.actionHandler1)
        importAction2.triggered.connect(self.actionHandler2)
        #action装入menu
        importMenu.addAction(importAction1)
        importMenu.addAction(importAction2)
        fileMenu.addAction(newAction)
        #装入总menu
        fileMenu.addMenu(importMenu)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('菜单')
        self.show()
    def newaction(self):
        print('新建')
    def actionHandler1(self):
        print('从pdf导入')

    def actionHandler2(self):
        print('从word导入')

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Menu()
    sys.exit(app.exec_())







