"""
插入排序
时间复杂度：最好情况下为O（n），最坏情况及平均情况为O（n*n）
空间复杂度：O（1）
稳定性：稳定
"""


def insert_sort(my_list):
    for i in range(1, len(my_list)):
        j = i-1
        if my_list[i] < my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            j = j-1
            while j >= 0 and my_list[j] > temp:
                my_list[j+1] = my_list[j]
                j = j-1
            my_list[j+1] = temp
    return my_list


unsorted_list = [38, 65, 97, 76, 13, 27, 49]
print(insert_sort(unsorted_list))
