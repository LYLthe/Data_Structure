"""
归并排序
时间复杂度：O（nlog2n）
空间复杂度：O（1）
稳定性：稳定
"""


def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] < arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) < 2:
            return array
        else:
            mid = len(array)//2
            arr_l = recursive(array[:mid])
            arr_r = recursive(array[mid:])
            return merge_arr(arr_l, arr_r)

    return recursive(array)


list_1 = [10, 45, 23, 47, 21]
print(merge_sort(list_1))
