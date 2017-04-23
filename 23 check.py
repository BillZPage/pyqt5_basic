# -*- coding: utf-8 -*-

# 复选框组件有两种状态：选中和未选中。它是由一个选择框和一个标签组成的。一个应用中，复选框是典型的用来代表有效或无效状态的组件。

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # 我们需要设置窗口标题，所以我们必须选中复选框。如果不选中复选框，默认情况下复选框不会被选中所以窗口标题也不会被设置。
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())