#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/30 22:22
# @Site    : 
# @File    : _config.py
# @Software: PyCharm

import os

class Path:
    '路径类的配置文件'
    root = os.path.dirname(os.getcwd())
    db = root+ r'\db'
    input = root+ r'\input'
    output = root+ r'\output'




