#！/usr/bin/env/ python
# -*- coding:utf-8 -*-
# @Time     :2018/5/3 10:10
# @Author   :xiongyaokun
# @Site     :
# @File     :unique_set.py
# @Software :PyCharm


def unique(l):
    """l is a list,"""
    ls = set(l)
    return ls


if __name__ == "__main__":
    l = [1, 3, 6, 9, 3, 4, 1, 3]
    print(unique(l))
