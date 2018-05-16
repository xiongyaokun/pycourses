#！/usr/bin/env/ python
# -*- coding:utf-8 -*-
# @Time     :2018/5/3 7:22
# @Author   :xiongyaokun
# @Site     :
# @File     :unique.py
# @Software :PyCharm

import random
import time


# 方法一：先搜索出重复元素的索引，按照索引排除重复元素
def unique(l):
    """This function get a list input, will remove the repeat elements from the list, finally
    return a unique list!
    """
    new_list = []
    index_list = []
    for a in range(len(l)):
        if a not in index_list:
            new_list.append(l[a])
            for b in range(a+1, len(l)):
                if l[b] == l[a]:
                    index_list.append(b)
    print("Game over!")
    return new_list


if __name__ == "__main__":
    test = [1, 2, 3, 3, 6, 9, 5, 1, 4, 2]
    t = list(range(10000))
    random.shuffle(list(range(10000)))

    # print(unique(test))

    # 测试程序运行时间
    start_time = time.time()
    unique(t)
    end_time = time.time()
    print('It costs {} seconds!'.format(end_time-start_time))
