#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : string_operation.py
# Author: gsm
# Date  : 2020/5/6
import string

def test_string():
    var1 = 'Hello World'
    var2 = 'python'
    print var1[0]
    print var1 + ' ' + var2  # 拼接字符串
    print 'H' in var1  # 像列表一样操作字符串
    print 'H' in var2
    print "The company I work for is %s and was founded in %d by Mr Ding!" % ('NetEase', 1997)
    var3 = ' Space '
    print string.strip(var3)  # string类中有许多内置函数用于操作字符串
    print string.strip(string.upper(var3))


if __name__ == '__main__':
    test_string()
