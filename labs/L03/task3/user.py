"""
Реалізуйте алгоритм пошуку номеру найпершого входження до заданого масиву, заданого числа x.
Якщо заданий елемент відсутній у списку - поверніть номер першого елементу, що більший за число x:
                            array[i] >= x
"""


def bsearch_leftmost(array, x):
    """ Бінарний пошук для відшукання найпершого входження заданого числа

    :param array: Відсортований за неспаданням масив цілих чисел
    :param x:     Шукане число
    :return:      Номер шуканого елемента у масиві
    """
    left = 0            # ліва границя пошуку
    right = len(array)  # права границя пошуку
    while left < right:
        m = left + (right - left) // 2  # Середина
        if array[m] < x:
            left = m + 1
        else:
            right = m

    return left
    # return 0


if __name__ == '__main__':
    myarray = [
        1, 1, 1, 1, 1, 4, 4, 4, 4, 4,
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
        5, 5, 5, 5, 5, 9, 9, 9
    ]

    res = bsearch_leftmost(myarray, 5)
    res = bsearch_leftmost(myarray, 3)
    res = bsearch_leftmost(myarray, 90)
    res = bsearch_leftmost(myarray, 0)
    print(res)