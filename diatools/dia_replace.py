#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import sys
from PyQt5 import QtWidgets

from diatools import files_tool

def arg_parser():
    parser = argparse.ArgumentParser(
            description=''' заменяет миниатюру на указанную
            gui - PyQt5
            ''')
    parser.add_argument('miniature',
                        help='путь к миниаюре', type=str)
    return parser

def get_diafilm_dir(miniature_path):

    dir_name, dia_name = os.path.split(os.path.splitext(miniature_path)[0])
    config_name = files_tool.DATA_FILE_NAME
    config = os.path.join(dir_name, config_name)
    conf_obj = files_tool.Pickle(config)
    data = conf_obj.load()
    diafilm = data[dia_name]['dia_dir']
    size = data[dia_name]['size']
    return miniature_path + "\n" + diafilm + "\n" + str(size)

class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.resize(700, 300)



def main():
    app = QtWidgets.QApplication(sys.argv)
    wind = Widget()
    parser = arg_parser()
    arg = parser.parse_args()
    path = arg.miniature
    text = get_diafilm_dir(path)
    wind.setText(text)
    wind.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()