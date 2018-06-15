"""
快速排序
时间复杂度：O（nlog2n）
空间复杂度：O(nlog2n)
稳定性：不稳定
"""


def quick_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        pivlot = my_list[0]
        less = [i for i in my_list[1:] if i <= pivlot]
        greater = [i for i in my_list[1:] if i > pivlot]
        return quick_sort(less) + [pivlot] + quick_sort(greater)


list_1 = [10, 5, 2, 3]
print(quick_sort(list_1))
