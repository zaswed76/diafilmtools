#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

join = os.path.join

IMAGEEXTS = ['png', 'jpg', 'jpeg']

def first_img(names_lst, ext_lst=None):
    """
    получает список строк и возвращает первую совпавшую с одним из расщирений
    список names_lst может быть отсортирован
    :param names_lst: list < str [str, ...]
    :param ext_lst: list < str [ext1, ext2, ...]
    :return: str первое совпадение с концом строки
    """
    if ext_lst is None:
        ext_lst = IMAGEEXTS
    s = "|".join(ext_lst)
    ext_pattern = re.compile('{}$'.format(s), re.IGNORECASE)
    for n in names_lst:
        if re.search(ext_pattern, n) is not None:
            return n


def files_for_thumbnails(directory, ext_lst=None):
    """

    каталог должен содержать каталоги с файлами
    с одним уровнем вложенности
    :param directory: str путь к каталогу с диафильмами
    :param ext_lst: list < str [ext1, ext2, ...]
    :return: list < str  полные пути к файлам
    """
    lst = []
    for dn in sorted(os.listdir(directory)):
        d = join(directory, dn)
        lst.append(
            join(d, first_img(sorted(os.listdir(d)), ext_lst)))
    return lst
