#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
fl = "/home/sergk/project/diafilmtools/diafilmtools/examples/zderg"

pat = re.compile('\d+\n$')

with open(fl, "r") as f:
    lst = f.readlines()

res = []
for s in lst:
    if not pat.match(s):
        res.append(s)

with open(fl + "_copy", "w") as f:
    f.writelines(res)






