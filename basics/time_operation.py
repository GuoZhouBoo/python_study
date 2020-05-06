#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : time_operation.py
# Author: gsm
# Date  : 2020/5/6
import time
import calendar


def test_time():
    ticks = time.time()
    print "当前时间戳为:", ticks
    localtime = time.localtime(time.time())
    print "本地时间为 :", localtime
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 将格式字符串转换为时间戳
    a = "Sat May 5 20:20:20 2020"
    print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
    cal = calendar.month(2020, 5)
    print
    print "以下输出2020年5月份的日历:"
    print cal


if __name__ == '__main__':
    test_time()
