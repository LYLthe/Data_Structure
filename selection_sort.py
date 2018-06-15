"""
选择排序
最优时间复杂度：O（n*n）
最坏时间复杂度：O（n*n）
稳定性：不稳定（考虑升序每次选择最大的情况）
"""


def select_sort(my_list):
    for i in range(len(my_list)):
        smallest = i
        for j in range(i+1, len(my_list)):
            if my_list[smallest] > my_list[j]:
                smallest = j
        my_list[smallest], my_list[i] = my_list[i], my_list[smallest]
    return my_list


arr = [10, 5, 84, 4, 3]
print(select_sort(arr))
arr_1 = [12, 4, 2, 68, 23, 68, 24]
print(select_sort(arr_1))
