#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : container.py
# Author: gsm
# Date  : 2020/5/6


def test_list():
    list1 = [1, 2, 3, 4, '5']
    print list1
    print list1[0]  # 输出第0个元素
    print list1[0:3]  # 输出第1-3个元素
    print list1[0:]  # 输出从0到最后的元素
    print list1[0:-1]  # 输出从0到最后第二元素
    print '-----------------'


def test_tuple():
    # 元组无法被二次赋值，相当于一个只读列表
    tuple1 = ('runoob', 786, 2.23, 'john', 70.2)
    tinytuple = (123, 'john')

    print tuple1  # 输出完整元组
    print tuple1[0]  # 输出元组的第一个元素
    print tuple1[1:3]  # 输出第二个至第四个（不包含）的元素
    print tuple1[2:]  # 输出从第三个开始至列表末尾的所有元素
    print tinytuple * 2  # 输出元组两次
    print tuple1 + tinytuple  # 打印组合的元组
    print '-----------------'


def test_dict():
    dict1 = {}
    dict1['one'] = "This is one"
    dict1[2] = "This is two"

    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

    print dict1['one']  # 输出键为'one' 的值
    print dict1[2]  # 输出键为 2 的值
    print tinydict  # 输出完整的字典
    print tinydict.keys()  # 输出所有键
    print tinydict.values()  # 输出所有值
    print '-----------------'


if __name__ == '__main__':
    test_list()
    test_tuple()
    test_dict()
