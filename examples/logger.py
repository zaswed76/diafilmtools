#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

FORMAT = "----------\nfilename > %(filename)s| dunc > %(funcName)s| %(asctime)s| %(message)s "
logging.basicConfig(filename="log", format=FORMAT)


def d(p):
    try:
        with open(p, "r") as f:
            return f.readlines()
    except Exception as m:
        logging.exception(m)
        sys.exit()


d("aaaa")