#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def arg_parser():
    parser = argparse.ArgumentParser(
        description='коротко о программе')
    parser.add_argument('diadir',
                        help='путь к каталогу с дифаильмами')
    parser.add_argument('target',
                        help='куда сохранять миниатюры')
    parser.add_argument('size', help='размер миниатюры')
    parser.add_argument('-r', dest='resample', default=2,
                        choices=['0', '1', '2', '3'], help='''сглаживание целое число 0 - 3
    чем больше тем качественей но дольше''')
    return parser

if __name__ == '__main__':
    parser = arg_parser()
    namespace = parser.parse_args()
    print(namespace)