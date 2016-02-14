#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image


def _progress(lst):
    return lst


printer = False
try:
    from tqdm import tqdm

    progress = tqdm
except:
    progress = _progress
    printer = True

RESAMPLE_NUM = [
    Image.NEAREST,
    Image.BILINEAR,
    Image.BICUBIC,
    Image.ANTIALIAS
]
DEFAULT_EXT = '.jpg'


def thumbnail(source, target, size, resample=2):
    img = Image.open(source)
    img.thumbnail((size, size), resample=RESAMPLE_NUM[resample])
    img.save(target)


def thumbnail_seq(**kwargs):
    for key, v in kwargs.items():
        thumbnail(v['source_file'], v['target_file'], v['size'],
                  resample=v['resample'])
        print(key)
