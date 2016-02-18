#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

from diatools.lib import image_tool

SPACING = 30
DEFAULT_COLUMN = 4
SIZE_IMAGE = 250
MARGING = (20, 20, 20, 20)
GRID_MARGING = (0, 0, 0, 0)

def get_number_of_lines(leng, col):
    return math.ceil(leng / col)


class Cell(QtWidgets.QLabel):
    click = pyqtSignal(str)

    def __init__(self, path=None, *__args):
        super().__init__(*__args)
        self.path = path
        self.setAlignment(QtCore.Qt.AlignCenter)
        if self.path:
            self.set_image()

    def mousePressEvent(self, QMouseEvent):
        self.click.emit(self.path)

    def set_image(self):
        self.setPixmap(QtGui.QPixmap(self.path).scaled(SIZE_IMAGE, SIZE_IMAGE, 1, 1))


class Grid(QtWidgets.QFrame):
    def __init__(self, parent, file_list, lines):
        super().__init__()
        self.parent = parent
        self.file_list = file_list
        self.lines = lines
        box = QtWidgets.QVBoxLayout(self)
        box.setContentsMargins(*MARGING)
        box.setSpacing(0)

        self.grid = QtWidgets.QGridLayout()
        self.grid.setContentsMargins(*GRID_MARGING)
        self.grid.setSpacing(SPACING)

        box.addLayout(self.grid)
        self.create_grid()

    def create_grid(self):
        n = 0
        cell = dict()
        for x in range(self.lines):
            for y in range(DEFAULT_COLUMN):
                try:
                    cell[(x, y)] = Cell(self.file_list[n])
                except IndexError:
                    cell[(x, y)] = Cell()
                cell[(x, y)].click.connect(self.parent.change_image)
                n += 1
                self.grid.addWidget(cell[(x, y)], x, y)


class Widget(QtWidgets.QFrame):
    def __init__(self, lst, target, size_miniature, resample):
        super().__init__()
        self.target = target
        self.resample = resample
        self.size_miniature = size_miniature
        self.file_lst = lst
        box = self.box(0, (0, 0, 0, 0), self)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        box.addWidget(self.scroll)
        lines = get_number_of_lines(len(self.file_lst), DEFAULT_COLUMN)
        self.update_grid(self.file_lst, lines)

    def update_grid(self, lst, lines):
        self.grid = Grid(self, lst, lines)
        self.scroll.setWidget(self.grid)

    @property
    def recommended_size(self):
        return self.grid.width() + SPACING

    def box(self, spacin, margin, parent):
        box = QtWidgets.QVBoxLayout(parent)
        box.setContentsMargins(*margin)
        box.setSpacing(spacin)
        return box

    def change_image(self, path):
        image_tool.thumbnail(path, self.target, self.size_miniature,
                             self.resample)
        self.close()


if __name__ == '__main__':
    pass
