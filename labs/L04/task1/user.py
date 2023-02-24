"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""


def solve(f, c, a, b):
    """ Для неспадної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """

    left = a
    right = b

    while True:
        m = (left + right) / 2

        if left == m or right == m:  # безпосереднє сусідство двох чисел з плаваючою крапкою
            break

        if f(m) < c:
            left = m
        else:
            right = m

        # if abs(right - left) < 0.0000000000001:  # точність по аргументу
        #     break
        # if abs(abs(f(m) - c)) < 0.0000000000001:   # точність по значенню
        #     break


    return left


def solve_decreasing(f, c, a, b):
    """ Для незростаючої на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    left = a
    right = b

    while True:
        m = (left + right) / 2

        if left == m or right == m:  # безпосереднє сусідство двох чисел з плаваючою крапкою
            break

        if f(m) > c:
            left = m
        else:
            right = m

        # if abs(right - left) < 0.0000000000001:  # точність по аргументу
        #     break
        # if abs(abs(f(m) - c)) < 0.0000000000001:   # точність по значенню
        #     break

    return left
