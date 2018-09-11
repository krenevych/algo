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
    l = a                 # лівий кінець відрізка
    r = b                 # правий кінець відрізка

    m = (l + r) / 2.0     # середина відрізка [l,r]
    while l != m and m != r:
        if f(m) < c:
            l = m  # [l,r] = [x,r]
        else:
            r = m  # [l,r] = [l,x]
        m = (l + r) / 2.0  # середина відрізка [l,r]

    return l


if __name__ == "__main__":
    print(binary_continuous(lambda x: math.tan(x) - 2.0 * x, 0, 0.5, 1.5))
