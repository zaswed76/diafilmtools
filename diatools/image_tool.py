#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image

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

def thumbnail_seq(source_lst, target_dir, size, resample=2, append="", default_ext=None):
    if default_ext is None:
        default_ext = DEFAULT_EXT
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    for s_path in source_lst:
        name = os.path.basename(os.path.dirname(s_path)) + append + default_ext
        target_path = os.path.join(target_dir, name)
        thumbnail(s_path, target_path, size, resample)
