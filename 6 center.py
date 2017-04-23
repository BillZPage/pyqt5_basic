# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)

        # 将窗口居中放置的代码在自定义的center()
        # 方法中。
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 我们获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        qr = self.frameGeometry()

        # 我们算出相对于显示器的绝对值。并且从这个绝对值中，我们获得了屏幕中心点。
        cp = QDesktopWidget().availableGeometry().center()

        # 我们的矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。矩形的大小并不会改变。
        qr.moveCenter(cp)

        # 我们移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())