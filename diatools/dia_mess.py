#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from diatools import settings
from diatools.lib import files_tool

def miniature_data(path):
    db_obj = files_tool.Pickle(path)
    return db_obj.load()

def search_diafilm(db, name):
    lst = []

    p = re.compile(name, re.IGNORECASE)
    for dia in db.keys():
        if p.search(dia):
            lst.append(dia)
    if lst:
        return "\n".join(lst), True
    else:
        return name, False

def get_message(mess, flag):
    if flag:
        message = """Найдены такие диафильмы:
        {}""".format(mess)
    else:
        message = "диафльм с текстом - < {} >\nне найден!".format(mess)
    return message, flag

def to_normalize_text(text):
    return text.strip()

class Widget(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #FAFAFA")
        font = QtGui.QFont("Helvetica", 22)
        self.setFont(font)
        self.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

    def set_text(self, text, flag):
        if flag:
            self.setStyleSheet("color: #09642F")
        else:
            self.setStyleSheet("color: #BD1741")
        self.setText(text)



def main():
    app = QtWidgets.QApplication(sys.argv)
    widg = Widget()
    widg.show()
    clipboard = QtWidgets.QApplication.clipboard()
    originalText = to_normalize_text(clipboard.text())
    sett= settings.Settings()
    conf = sett.config()
    path_pcl = conf["data"]
    mess, flag = search_diafilm(miniature_data(path_pcl), originalText)

    widg.set_text(*get_message(mess, flag))

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()