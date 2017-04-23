# -*- coding: utf-8 -*-
# QColorDialog类提供了一个用于选择颜色的对话框组件。

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor

# 例子中显示了一个按钮和一个QFrame。将QFrame组件的背景设置为黑色。使用颜色选择框类，我们可以改变它的颜色。
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 初始化QtGuiQFrame组件的背景颜色。
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    # 如果我们选中一个颜色并且点了ok按钮，会返回一个有效的颜色值。如果我们点击了Cancel按钮，不会返回选中的颜色值。我们使用样式表来定义背景颜色。
    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())