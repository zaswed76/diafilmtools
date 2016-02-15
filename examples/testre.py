#!/usr/bin/env python
# -*- coding: utf-8 -*-

d_old = dict(a=1, s=2)

d_new = dict(c=3, a=999)

d_old.update(d_new)

print(d_old)