#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : file_io.py
# Author: gsm
# Date  : 2020/5/6


def file_operation(file_name):
    file = open(file_name, 'w')
    print "文件名: ", file.name
    print "是否已关闭 : ", file.closed
    print "访问模式 : ", file.mode
    file.write('%s%s\n' % ('a', 'a'))
    file.close()  # 使用pandas操作文件会更加简单


if __name__ == '__main__':
    input_str = raw_input("请输入：")  # 从标准输入读取一个行，并返回一个字符串
    print "你输入的内容是: ", input_str
    input_str = input("请输入：")  # 与raw_input基本类似，但input 可以接收一个Python表达式作为输入，并将运算结果返回
    print "你输入的内容是: ", input_str
