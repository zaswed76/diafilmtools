#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import re

join = os.path.join

IMAGEEXTS = ['png', 'jpg', 'jpeg']
DEFAULT_EXT = '.jpg'
DATA_FILE_NAME = "data.pkl"


def collect_files_by_extensions(directory, ext_lst):
    lst = []
    files_lst = [os.path.join(directory, p) for p in os.listdir(directory)]
    s = "|".join(ext_lst)
    ext_pattern = re.compile('{}$'.format(s), re.IGNORECASE)
    for n in files_lst:
        if re.search(ext_pattern, n) is not None:
            lst.append(n)
    return lst


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
                         overwrite=False,
                         update=False):
    """

    :param source_dir:
    :param target_dir:
    :param size:
    :param resample: int choices (0, 1, 2, 3) - сглаживание
    :param data: dict конфигурационный файл описывающий уже существующие миниатюры
    :param ext_lst: допустимые расширения
    :param default_ext:
    :param overwrite:
    :param update:
    :return: tuple < (dict, dict)
    !!! две точки выхода
    """
    source_dir = os.path.abspath(source_dir)
    data_old = data
    data_new = dict()

    if ext_lst is None:
        ext_lst = IMAGEEXTS

    if update:
        for name, opt_dict in data_old.items():
            opt_dict.update(dict(size=size, resample=resample))
        return data_old, data_old

    for dn in sorted(os.listdir(source_dir)):

        d = join(source_dir, dn)
        source_file = join(d,
                           first_img(sorted(os.listdir(d)), ext_lst))
        name_file = path_to_name(source_file)

        dia_dir = os.path.join(source_dir,
                               name_file)

        target_file = os.path.join(target_dir,
                                   name_file + default_ext)

        # todo требуется рефакторинг

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

    """
    получить список расширений всех файлов в директории
    :param directory:
    :return:
    """
    exts = set()
    for root, dirs, files in os.walk(directory):
        for name in files:
            fullname = os.path.join(root,
                                    name)  # получаем полное имя файла
            exts.add(os.path.splitext(fullname)[1])
    return exts

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
