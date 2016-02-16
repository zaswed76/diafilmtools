#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal

from diatools import files_tool

SIZE_IMAGE = 250
MARGIN = 20



def arg_parser():
    parser = argparse.ArgumentParser(
            description=''' заменяет миниатюру на указанную
            gui - PyQt5
            ''')
    parser.add_argument('miniature',
                        help='путь к миниаюре', type=str)
    return parser


def get_diafilm_dir(miniature_path, ):
    dir_name, dia_name = os.path.split(
            os.path.splitext(miniature_path)[0])
    config_name = files_tool.DATA_FILE_NAME
    config = os.path.join(dir_name, config_name)
    conf_obj = files_tool.Pickle(config)
    data = conf_obj.load()
    diafilm = data[dia_name]['dia_dir']
    size = data[dia_name]['size']
    files = files_tool.collect_files_by_extensions(diafilm,
                                                   files_tool.IMAGEEXTS,
                                                   sort=True,
                                                   reverse=False)
    return files


class Cell(QtWidgets.QLabel):
    click = pyqtSignal(str)

    def __init__(self, size, path_image=None):
        super().__init__()
        self.path_image = path_image
        if path_image is not None:
            pixmap = QtGui.QPixmap(path_image).scaled(size,
                                                      size,
                                                      1, 1)
            self.setPixmap(pixmap)
        else:
            self.setFixedWidth(size)
            self.setFixedHeight(size)
            self.setStyleSheet("background-color: lightgrey")

    def mousePressEvent(self, QMouseEvent):
        self.click.emit(self.path_image)


class DisplayGrid(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)



    def create_grid(self, img_lst, column, img_size):
        lines = int(len(img_lst) / column + 1)
        width = column * img_size + ((column -1) * MARGIN)
        print(column, img_size, width)
        height = lines * img_size

        n = 0
        for x in range(lines):
            for y in range(column):
                try:
                    img = img_lst[n]
                    n += 1
                except IndexError:
                    img = None
                label = Cell(img_size, img)
                # label.click.connect(self.change_image)
                self.grid.addWidget(label, x, y)
        return width, height


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        box = QtWidgets.QVBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        box.setSpacing(0)
        self.display = DisplayGrid()
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        box.addWidget(self.scroll)
        self.scroll.setWidget(self.display)






    def create_grid(self, lst, column, size):
        width, height = self.display.create_grid(lst, column, size)
        self.display.setFixedSize(width, height)
        print(width)
        self.setFixedWidth(width + 100)
        self.setMinimumHeight(600)

    def change_image(self, path):
        # create_miniature(path, 240)
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = Widget()
    parser = arg_parser()
    arg = parser.parse_args()
    path = arg.miniature
    text = get_diafilm_dir(path)
    wind.create_grid(text, 3, 200)
    wind.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
