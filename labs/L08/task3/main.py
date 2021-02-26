import time

import numpy
import user


def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            errors += 1

    print("Errors:       ", errors)


def testSort(base, sort):
    s = numpy.copy(base)
    t = time.process_time()
    sort(s)
    dt = time.process_time() - t
    print('Sorting method: ', sort)
    print('Sorting time: ', dt)
    checkResult(s)


sorting_method = [user.bubble_sort,
                  user.bubble_sort_optimized,
                  user.selection_sort,
                  user.insertion_sort,
                  user.merge_sort,
                  user.quick_sort]


def test():
    base = numpy.random.randint(0, 100000, user.N)

    print(" == Randomly generated array == ")
    for func in sorting_method:
        testSort(base, func)

    sorted_increasing = numpy.copy(base)
    sorted_increasing.sort()
    print("\n == Sorted (inc) array == ")
    for func in sorting_method:
        testSort(sorted_increasing, func)

    sorted_decreasing = sorted_increasing[::-1]
    print("\n == Sorted (dec) array == ")
    for func in sorting_method:
        testSort(sorted_decreasing, func)


if __name__ == "__main__":
    test()
