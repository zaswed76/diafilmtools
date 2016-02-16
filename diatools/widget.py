#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets


class Cell(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet("background-color: grey")
        self.setFixedSize(100, 100)


class Grid(QtWidgets.QFrame):
    def __init__(self, lst, spacing, margins):
        super().__init__()
        self.lst = lst
        box = QtWidgets.QVBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        box.setSpacing(0)

        self.grid = QtWidgets.QGridLayout()
        self.grid.setContentsMargins(*margins)
        self.grid.setSpacing(spacing)

        box.addLayout(self.grid)
        self.create_grid()

    def create_grid(self):
        cell = dict()
        for x in range(23):
            for y in range(3):
                cell[(x, y)] = Cell(str((x, y)))
                self.grid.addWidget(cell[(x, y)], x, y)

    def calc_table(self, len_list, width_img, column, spacing,
                   marging):
        wind_size = (column * width_img) + (
        (column - 1) * spacing) + (marging * 2)


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        box = self.box(0, (0, 0, 0, 0), self)
        self.block_flag = True

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        box.addWidget(self.scroll)
        self.update_grid(3)

    def update_grid(self, c):
        self.grid = Grid(c)
        self.scroll.setWidget(self.grid)

    def resizeEvent(self, QResizeEvent):
        size = QResizeEvent.size()
        w, h = size.width(), size.width()
        if self.block_flag:
            if w > 900:
                self.update_grid(4)
                self.block_flag = False

    def box(self, spacin, margin, parent):
        box = QtWidgets.QVBoxLayout(parent)
        box.setContentsMargins(*margin)
        box.setSpacing(spacin)
        return box


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
