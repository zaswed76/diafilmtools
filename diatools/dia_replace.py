#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal

from diatools import files_tool

def arg_parser():
    parser = argparse.ArgumentParser(
            description=''' заменяет миниатюру на указанную
            gui - PyQt5
            ''')
    parser.add_argument('miniature',
                        help='путь к миниаюре', type=str)
    return parser

def get_diafilm_dir(miniature_path, ):

    dir_name, dia_name = os.path.split(os.path.splitext(miniature_path)[0])
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
    def __init__(self, path_image=None):
        super().__init__()
        self.path_image = path_image
        print(self.path_image)

        self.setScaledContents(True)
        if path_image is not None:
            pixmap = QtGui.QPixmap(path_image).scaled(280, 280, 1, 1)
            self.setPixmap(pixmap)
        else:
            self.resize(280, 280)
            self.setStyleSheet("background-color: lightgrey")

    def mousePressEvent(self, QMouseEvent):
        self.click.emit(self.path_image)

class DisplayGrid(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setSpacing(15)

    def create_grid(self, img_lst):
        n = 0
        for x in range(3):
            for y in range(4):
                try:
                    img = img_lst[n]
                    n += 1
                except IndexError:
                    img = None
                label = Cell(img)
                # label.click.connect(self.change_image)
                self.grid.addWidget(label, x, y)


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        box = QtWidgets.QVBoxLayout(self)
        self.display = DisplayGrid()
        self.display.setScaledContents(True)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        box.addWidget(self.scroll, 1)
        self.scroll.setWidget(self.display)

        self.resize(700, 300)

    def set_text(self, lst):
        self.display.create_grid(lst)

    def change_image(self, path):
        create_miniature(path, 240)
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = Widget()
    parser = arg_parser()
    arg = parser.parse_args()
    path = arg.miniature
    text = get_diafilm_dir(path)
    wind.set_text(text)
    wind.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()