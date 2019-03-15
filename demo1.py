#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2018/9/12 16:04
#@Author: zhangdelong
#@File  : demo1.py
name = input("Please input your name:")
# 打印输出有下面三种方法，最常用的是第一种
print("hello {0}".format(name))
print("hello" + name)
print("hello %s" %name)