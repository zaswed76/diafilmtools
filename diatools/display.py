#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess
import argparse
from diatools import files_tool, dia_min

DEFAULT_DISPLAY_PROGRAM = 'mcomix -f'




def arg_parser():
    parser = argparse.ArgumentParser(
            description='программа для ппросмотра дифильмов')
    parser.add_argument('miniature',
                        help='путь к каталогу с миниатюрами')

    parser.add_argument('-с', dest='command', default=DEFAULT_DISPLAY_PROGRAM, type=str,
                        help=''' команда для просмотра''')


    return parser

def get_diafilm(miniature_path):
    miniature_dir, name_ext = os.path.split(miniature_path)
    name = os.path.splitext(name_ext)[0]
    db_file = os.path.join(miniature_dir, dia_min.DATA_FILE_NAME)
    db_obj = files_tool.Pickle(db_file)
    data = db_obj.load()
    dia_dir =data[name]['dia_dir']
    return dia_dir

def run_diafilm(display, diafilm):
    display.append(diafilm)
    subprocess.call(display)


def main():
    parser = arg_parser()
    arg = parser.parse_args()
    diafilm = get_diafilm(arg.miniature)
    display = arg.command.split()
    run_diafilm(display, diafilm)



if __name__ == '__main__':
    main()