# -*- coding: utf-8 -*-
#主界面

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication,QWidget
from PyQt5.QtWidgets import QTabWidget,QTabBar
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtGui import QIcon

class CommTab(QTabBar):
    def __init__(self,parent=None):
        QTabBar.__init__(self, parent)
        print('CommTab')

        qbtn = QPushButton('Quit', self)
        # qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)


# 我们创建了有一个菜单项的菜单栏。这个菜单项包含一个选中后中断应用的动作。
class ZConnect(QMainWindow):
    def __init__(self):
        super().__init__()

        #新建连接
        self.newAction = QAction(QIcon('resource/new.png'), '&New', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip('新建连接')
        self.newAction.triggered.connect(self.NewComm)
        print('new')

        #重连连接
        self.reloadAction = QAction(QIcon('resource/reload.png'), '&Reload', self)
        self.reloadAction.setShortcut('Ctrl+R')
        self.reloadAction.setStatusTip('重建连接')
        # self.reloadAction.triggered.connect(qApp.quit)
        print('reload')

        #添加菜单栏
        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.reloadAction)

        #添加工具栏
        self.toolbar = self.addToolBar('New')
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.reloadAction)

        #添加状态栏
        self.statusBar()

        self.tabwidget = QTabWidget()
        # 设置tabwidget的bar
        # self.tabwidget.setTabBar(CommTab())
        # # 允许tab点击关闭
        self.tabwidget.setTabsClosable(True)

        #设置主窗口widget
        self.setCentralWidget(self.tabwidget)
        self.setWindowTitle('ZConnect')
        self.show()

    def NewComm(self):
        self.tabwidget.addTab(CommTab(), "tab1")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    zc = ZConnect()
    sys.exit(app.exec_())