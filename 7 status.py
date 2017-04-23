# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

# 状态栏又QMainWindow组件帮助创建完成（依赖于QMainWindow组件）。
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 为了得到状态栏，我们调用了QtGui.QMainWindow类的statusBar()
        # 方法。第一次调用这个方法创建了一个状态栏。随后方法返回状态栏对象。然后用showMessage()
        # 方法在状态栏上显示一些信息。
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())