#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

LENG = 18
COL = 3
WIDTH = 420
WIDTH_IMAGE = 100
PERCENTAGE = 10


def get_indent(width, parc):
    return int((width / 100) * parc)

def get_number_of_lines(leng, col):
    return math.ceil(leng / col)


def get_number_of_columns(width_wind, width_image, indent):
    return math.floor((width_wind / (width_image + indent)))

indent = get_indent(WIDTH, PERCENTAGE)
print(get_number_of_columns(WIDTH, WIDTH_IMAGE, indent))

class TableModel:
    def __init__(self, width_wind, width_block, spacing):
        self._columns = None
        self._lines = None
        self._width_wind = width_wind
        self._width_block = width_block
        self._spacing = spacing

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, col):
        self._columns = col

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, lines):
        self._lines = lines

    @property
    def width_wind(self):
        return self._width_wind

    @width_wind.setter
    def width_wind(self, width):
        self._width_wind = width

table = TableModel(400, 100, 10)

def resize(width):
    table.width_wind = width
    columns = table.columns
    lines = table.lines

if __name__ == '__main__':
    pass


