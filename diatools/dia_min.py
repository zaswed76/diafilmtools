#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import os

from diatools.lib import files_tool, image_tool

DATA_FILE_NAME = files_tool.DATA_FILE_NAME


class FileError(Exception): pass


def arg_parser():
    parser = argparse.ArgumentParser(
            description='''создаёт миниатюры в указанном каталоге.
            По умолчанию скрипт работает только на добавление,
            см. опцию - --write_mode

            ''')
    parser.add_argument('diadir',
                        help='путь к каталогу с дифаильмами')
    parser.add_argument('target',
                        help='куда сохранять миниатюры')
    parser.add_argument('size', type=int, help='размер миниатюры')
    parser.add_argument('-r', dest='resample', default=2, type=int,
                        choices=[0, 1, 2, 3], help='''сглаживание целое число 0 - 3
    чем больше тем качественей но дольше''')
    parser.add_argument('-f', '--valid_ext_file',
                        help='''файл с допустимыми расширениями,
                        перечисленными каждое с новой строки''')

    parser.add_argument('-app', '--append', default="",
                        help=''' добавить к имени миниатюры''')

    parser.add_argument('-e', '--default_ext',
                        help=''' расширение для сохранения''')

    # если не указан то возвращается False
    parser.add_argument('-m', '--write_mode', action='store_true',
                        help=''' если указать этот ключ то МИНИАТЮРЫ будут
                        перезаписаны с новыми параметрами,
                        но НЕ УДАЛЕНЫ, в случае удаления самого диафильма''')

    parser.add_argument('-u', '--update', action='store_true',
                        help=''' если указать этот ключ то миниатюры будут
                         обновлены исходя из данных путей старой базы,
                         но с новыми параметрами''')

    return parser


def create_config(dir):
    return


def main():
    parser = arg_parser()
    arg = parser.parse_args()

    if not os.path.isdir(arg.diadir):
        raise FileError("каталог {} - не найден !".format(arg.diadir))

    if not os.path.isdir(arg.target):
        os.makedirs(arg.target)
        print("был создан каталог - {}".format(arg.target))

    data_file = os.path.join(arg.target, DATA_FILE_NAME)
    db_obj = files_tool.Pickle(data_file)

    data_all, data_new = files_tool.files_for_thumbnails(arg.diadir,
                                                         arg.target,
                                                         arg.size,
                                                         arg.resample,
                                                         db_obj.load(),
                                                         ext_lst=arg.valid_ext_file,
                                                         overwrite=arg.write_mode,
                                                         update=arg.update)

    image_tool.thumbnail_seq(**data_new)

    db_obj.save(data_all)


if __name__ == '__main__':
    main()
