#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

leng = 18
col = 3

def calc(leng, col):
    return leng // col + bool(leng % col)

def calc2(leng, col):
    return math.ceil(leng / col)

print(calc2(leng, col))
