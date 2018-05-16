# ！/usr/bin/env/ python
# -*- coding:utf-8 -*-
# @Time     :2018/5/3 7:08
# @Author   :xiongyaokun
# @Site     :
# @File     :multip-table.py
# @Software :PyCharm


def multip():
    """This function create a Multiplication table!"""
    for a in range(1, 10):
        for b in range(1, a + 1):
            print('{}*{}={}'.format(b, a, b * a), '  ', end=''),
        print('\n')


if __name__ == "__main__":
    multip()
