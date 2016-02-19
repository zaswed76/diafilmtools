#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from PyQt5 import QtWidgets

from diatools.lib import files_tool, min_ggrid

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


def get_diafilm_data(miniature_path):
    dir_name, dia_name = os.path.split(
            os.path.splitext(miniature_path)[0])
    config_name = files_tool.DATA_FILE_NAME
    config = os.path.join(dir_name, config_name)
    conf_obj = files_tool.Pickle(config)
    data = conf_obj.load()
    diafilm = data[dia_name]['dia_dir']
    size = data[dia_name]['size']
    resample = data[dia_name]['resample']

    files = files_tool.collect_files_by_extensions(diafilm,
                                                   files_tool.IMAGEEXTS,
                                                   sort=True,
                                                   reverse=False)
    return files, size, resample


def main():
    app = QtWidgets.QApplication(sys.argv)
    parser = arg_parser()
    arg = parser.parse_args()
    path = arg.miniature
    files, size, resample = get_diafilm_data(path)
    files = files[:9]
    wind = min_ggrid.Widget(files, path, size, resample)
    wind.show()
    wind.setMinimumWidth(wind.recommended_size)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
