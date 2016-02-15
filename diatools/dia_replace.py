#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
from PyQt5 import QtWidgets

def arg_parser():
    parser = argparse.ArgumentParser(
            description=''' заменяет миниатюру на указанную
            gui - PyQt5
            ''')
    parser.add_argument('miniature',
                        help='путь к миниаюре', type=argparse.FileType())
    return parser

class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()



def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = Widget()
    parser = arg_parser()
    arg = parser.parse_args()
    wind.setText(arg.miniature)
    wind.show()
    sys.exit(app.exec_())