"""
冒泡排序
时间复杂度：O（n*n）
最优排序：O（n）
稳定性：稳定
"""

import time
import random


def new_num(my_list):
    for i in range(50):
        num = random.randint(0, 1000)
        my_list.append(num)
    return my_list


# 开始时间
start_time = time.time()


def bubble_sort_high(list_1):
    """升序排列"""
    for i in range(len(list_1)-1, 0, -1):
        for j in range(i):
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
    return list_1


def bubble_sort_low(list_2):
    """降序排列"""
    for i in range(len(list_2)-1, 0, -1):
        for j in range(i):
            if list_2[j] < list_2[j+1]:
                list_2[j], list_2[j+1] = list_2[j+1], list_2[j]
    return list_2


y_list = []
unsorted_list = new_num(y_list)
print(unsorted_list)
print("升序排列 ", bubble_sort_high(unsorted_list))
print("降序排列: ", bubble_sort_low(unsorted_list))
