#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import math

from PyQt5 import QtWidgets

def get_number_of_lines(leng, col):
    return math.ceil(leng / col)


class Cell(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet("background-color: grey")
        self.setFixedSize(100, 100)


class Grid(QtWidgets.QFrame):
    def __init__(self, columns, lines, spacing):
        super().__init__()

        self.columns = columns
        self.lines = lines
        box = QtWidgets.QVBoxLayout(self)
        box.setContentsMargins(20, 20, 20, 20)
        box.setSpacing(0)

        self.grid = QtWidgets.QGridLayout()
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(spacing)

        box.addLayout(self.grid)
        self.create_grid()

    def create_grid(self):
        cell = dict()
        for x in range(self.lines):
            for y in range(self.columns):
                cell[(x, y)] = Cell(str((x, y)))
                self.grid.addWidget(cell[(x, y)], x, y)

    def calc_table(self, len_list, width_img, column, spacing,
                   marging):
        wind_size = (column * width_img) + (
        (column - 1) * spacing) + (marging * 2)


class Widget(QtWidgets.QFrame):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst
        self.resize(500, 500)
        self.default_column = 4
        box = self.box(0, (0, 0, 0, 0), self)


        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        box.addWidget(self.scroll)
        lines = get_number_of_lines(len(self.lst), self.default_column)
        self.update_grid(self.default_column, lines, 30)

    def update_grid(self, columns, lines, spacing):
        self.grid = Grid(columns, lines, spacing)
        self.scroll.setWidget(self.grid)



    def box(self, spacin, margin, parent):
        box = QtWidgets.QVBoxLayout(parent)
        box.setContentsMargins(*margin)
        box.setSpacing(spacin)
        return box


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget(range(20))
    main.show()
    sys.exit(app.exec_())
