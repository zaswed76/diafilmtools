#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

t = "Андрюшкины игрушки (1900).jpg"

p = re.compile('Андрюшкины игрушки \(1900\).jpg')

print(p.search(t))