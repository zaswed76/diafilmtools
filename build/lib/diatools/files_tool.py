#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import pickle

join = os.path.join

IMAGEEXTS = ['png', 'jpg', 'jpeg']
DEFAULT_EXT = '.jpg'


def first_img(names_lst, ext_lst=None):
    """
    получает список строк и возвращает первую совпавшую с одним из расщирений
    список names_lst может быть отсортирован
    :param names_lst: list < str [str, ...]
    :param ext_lst: list < str [ext1, ext2, ...]
    :return: str первое совпадение с концом строки
    """
    s = "|".join(ext_lst)
    ext_pattern = re.compile('{}$'.format(s), re.IGNORECASE)
    for n in names_lst:
        if re.search(ext_pattern, n) is not None:
            return n


def path_to_name(path):
    return os.path.basename(os.path.dirname(path))


def files_for_thumbnails(source_dir, target_dir, size, resample, data,
                         ext_lst=None, default_ext=DEFAULT_EXT,
                         overwrite=False):
    """

    каталог должен содержать каталоги с файлами
    с одним уровнем вложенности
    :param source_dir: str путь к каталогу с диафильмами
    :param ext_lst: list < str [ext1, ext2, ...]
    :return: list < str  полные пути к файлам
    """

    source_dir = os.path.abspath(source_dir)
    data_old = data
    data_new = dict()

    if ext_lst is None:
        ext_lst = IMAGEEXTS

    for dn in sorted(os.listdir(source_dir)):
        d = join(source_dir, dn)
        source_file = join(d,
                           first_img(sorted(os.listdir(d)), ext_lst))
        name_file = path_to_name(source_file)

        dia_dir = os.path.join(source_dir,
                                   name_file)

        target_file = os.path.join(target_dir,
                                   name_file + default_ext)
        if overwrite:
            data_new[name_file] = dict(source_dir=source_dir,
                                           target_dir=target_dir,
                                           source_file=source_file,
                                           target_file=target_file,
                                           size=size,
                                           resample=resample,
                                           dia_dir=dia_dir)
        elif name_file not in data_old:
            data_new[name_file] = dict(source_dir=source_dir,
                                           target_dir=target_dir,
                                           source_file=source_file,
                                           target_file=target_file,
                                           size=size,
                                           resample=resample,
                                           dia_dir=dia_dir)

    data_old.update(data_new)

    return data_old, data_new


def len_dir(dir):
    return len(os.listdir(dir))


def ext_list(directory):
    exts = set()
    for root, dirs, files in os.walk(directory):
        for name in files:
            fullname = os.path.join(root,
                                    name)  # получаем полное имя файла
            exts.add(os.path.splitext(fullname)[1])
    return exts


def create_db(source_dir, target_dir, size_min, resample):
    pass

class Pickle:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            with open(self.path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return dict()

    def save(self, data):
        with open(self.path, 'wb') as f:
            pickle.dump(data, f)



if __name__ == '__main__':
    data_f = '/home/vostro/Изображения/diafilms/data.pkl'
    dobj = Pickle(data_f)
    print(dobj.load())



