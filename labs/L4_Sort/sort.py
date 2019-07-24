from source.T3_Find_Search.P2_Sort.L4_merge import merge_sort
from source.T3_Find_Search.P2_Sort.L5_quick import quick_sort


def qsort(v, left, right):
    if left >= right:
        return
    pivot = v[left + (right - left) // 2]
    i = left
    j = right
    while True:
        while v[i] < pivot:
            i += 1
        while pivot < v[j]:
            j -= 1
        if i >= j:
            break
        v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1

    qsort(v, left, j)
    qsort(v, j + 1, right)


def sort(array):
    """ Сортування масиву
    :param array: Масив
    :return:
    """
    pass  # TODO: implement
    # qsort(array, 0, len(array) - 1)
    # merge_sort(array)
    quick_sort(array)

