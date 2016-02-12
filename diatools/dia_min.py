#!/usr/bin/env python
# -*- coding: utf-8 -*-


import files_tool
import image_tool
import argparse

def arg_parser():
    parser = argparse.ArgumentParser(
        description='коротко о программе')
    parser.add_argument('diadir',
                        help='путь к каталогу с дифаильмами')
    parser.add_argument('target',
                        help='куда сохранять миниатюры')
    parser.add_argument('size', type=int,  help='размер миниатюры')
    parser.add_argument('-r', dest='resample', default=2, type=int,
                        choices=[0, 1, 2, 3], help='''сглаживание целое число 0 - 3
    чем больше тем качественей но дольше''')
    parser.add_argument('-f', '--ext_file',
                        help='''файл с допустимыми расширениями,
                        перечисленными каждое с новой строки''')

    parser.add_argument('-a', '--append', default="",
                        help=''' добавить к имени миниатюры''')

    parser.add_argument('-e', '--default_ext',
                        help=''' расширение для сохранения''')
    return parser

def create_miniature(source, target, size, resample=2, ext_list=None, append="", default_ext=None):
    first_files_lst = files_tool.files_for_thumbnails(source, ext_list)
    image_tool.thumbnail_seq(first_files_lst, target, size, resample, append=append, default_ext=default_ext)


if __name__ == '__main__':
    parser = arg_parser()
    arg = parser.parse_args()
    ext_list = None
    create_miniature(arg.diadir, arg.target, arg.size,
                           resample=arg.resample,
                           ext_list=ext_list,
                           append=arg.append,
                           default_ext=arg.default_ext)
