import math


def binary_continuous(f, c, a, b):
    """ Для монотонної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    left = a                  # лівий кінець відрізка
    right = b                 # правий кінець відрізка

    while True:
        m = (left + right) / 2.0  # середина відрізка [left,right]
        if left != m and m != right:
            break

        if f(m) < c:
            left = m   # [left,right] = [x,right]
        else:
            right = m  # [left,right] = [left,x]

    return left


if __name__ == "__main__":
    print(binary_continuous(lambda x: math.tan(x) - 2.0 * x, 0, 0.5, 1.5))
