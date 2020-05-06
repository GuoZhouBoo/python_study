#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : operator.py
# Author: gsm
# Date  : 2020/5/6


def test_assigning_operator():
    a, b, c = 2, 2, 3
    c = a + b
    print "1 - c 的值为：", c

    c += a
    print "2 - c 的值为：", c

    c *= a
    print "3 - c 的值为：", c

    c /= a
    print "4 - c 的值为：", c

    c = 3
    c %= a
    print "5 - c 的值为：", c

    c **= a
    print "6 - c 的值为：", c

    c //= a
    print "7 - c 的值为：", c

    print '--------------------------------'

    # c++


def test_bit_operator():
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    c = 0

    c = a & b  # 12 = 0000 1100
    print "1 - c 的值为：", c

    c = a | b  # 61 = 0011 1101
    print "2 - c 的值为：", c

    c = a ^ b  # 49 = 0011 0001
    print "3 - c 的值为：", c

    c = ~a  # -61 = 1100 0011
    print "4 - c 的值为：", c

    a = 60
    c = a << 1  # 左移一位相当于乘以2
    print "5 - c 的值为：", c

    a = 60
    c = a >> 1  # 右移一位相当于除以2
    print "6 - c 的值为：", c

    print '--------------------------------'


def test_special_operator():
    list1 = [1, 2, 3]
    print 1 in list1
    print 1 not in list1

    # is 相当于Java中的equals运算符，python中的==与Java中的一样，
    # 都是比较变量是否处于同一个内存空间（Java中是利用内存的hash值进行比较）
    a = 20
    b = 20
    if a is b:
        print "1 - a 和 b 有相同的标识"
    else:
        print "1 - a 和 b 没有相同的标识"

    if a is not b:
        print "2 - a 和 b 没有相同的标识"
    else:
        print "2 - a 和 b 有相同的标识"

    # 修改变量 b 的值
    b = 30
    if a is b:
        print "3 - a 和 b 有相同的标识"
    else:
        print "3 - a 和 b 没有相同的标识"

    if a is not b:
        print "4 - a 和 b 没有相同的标识"
    else:
        print "4 - a 和 b 有相同的标识"


if __name__ == '__main__':
    test_assigning_operator()
    test_bit_operator()
    test_special_operator()
