"""
简单选择排序
基本思想：在要排序的一组数中，选出最小（或者最大）的一个数与第1个位置的数交换；
然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换，依次类推，直到第n-1个元素（倒数第二个数）和
第n个元素（最后一个数）比较为止。
时间复杂度：O（n*n）
"""


def simple_select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


my_array = [23, 4, 1, 45]
print(simple_select_sort(my_array))
