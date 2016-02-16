#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    from PyQt4 import QtGui
except ImportError:
    from PyQt5 import QtWidgets as QtGui


class Widget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.label = []
        self.line_edit = QtGui.QLineEdit()
        self.line_edit.returnPressed.connect(self.set_text)
        self.box = QtGui.QVBoxLayout(self)
        self.box.addWidget(self.line_edit)

    def add_labels(self, number_of_label):
        for i in range(number_of_label):
            self.label.append(QtGui.QLabel())
            self.box.addWidget(self.label[i])
            self.label[i].setNum(i)

    def set_text(self):
        if self.counter < len(self.label):
            self.label[self.counter].clear()
            self.label[self.counter].setText(self.line_edit.text())
            self.line_edit.clear()
            self.counter += 1
        else:
            print('некуда писать')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Widget()
    main.add_labels(8)
    main.show()
    sys.exit(app.exec_())
