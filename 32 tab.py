# -*- coding: utf-8 -*-
#������

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


# ���Ǵ�������һ���˵���Ĳ˵���������˵������һ��ѡ�к��ж�Ӧ�õĶ�����
class ZConnect(QMainWindow):
    def __init__(self):
        super().__init__()

        #�½�����
        self.newAction = QAction(QIcon('resource/new.png'), '&New', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip('�½�����')
        self.newAction.triggered.connect(self.NewComm)
        print('new')

        #��������
        self.reloadAction = QAction(QIcon('resource/reload.png'), '&Reload', self)
        self.reloadAction.setShortcut('Ctrl+R')
        self.reloadAction.setStatusTip('�ؽ�����')
        # self.reloadAction.triggered.connect(qApp.quit)
        print('reload')

        #��Ӳ˵���
        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.reloadAction)

        #��ӹ�����
        self.toolbar = self.addToolBar('New')
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.reloadAction)

        #���״̬��
        self.statusBar()

        self.tabwidget = QTabWidget()
        # ����tabwidget��bar
        # self.tabwidget.setTabBar(CommTab())
        # # ����tab����ر�
        self.tabwidget.setTabsClosable(True)

        #����������widget
        self.setCentralWidget(self.tabwidget)
        self.setWindowTitle('ZConnect')
        self.show()

    def NewComm(self):
        self.tabwidget.addTab(CommTab(), "tab1")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    zc = ZConnect()
    sys.exit(app.exec_())