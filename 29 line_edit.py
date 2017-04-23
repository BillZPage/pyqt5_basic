# -*- coding: utf-8 -*-

# 单行文本编辑框组件允许输入单行的纯文本数据 。这个组件支持撤销、重做、剪切、粘贴、拖拽、拖动方法。

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 上面是onChanged()
    # 方法的实现，我们设置了标签的显示文本。我们调用了adjustSize()
    # 方法来调整标签相对于显示的文本的长度。
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())