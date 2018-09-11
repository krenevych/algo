def binary_search(array, x):
    """ Бінарний пошук у масиві

    :param array: Список елементів
    :param x: Шуканий елемент
    :return: True, якщо шуканий елемент знайдено
    """
    l = 0          # Індекс лівого елементу
    r = len(array) - 1 # Індекс правого елементу
    alist = array[l:r + 1]
    print(alist)
    while r > l:

        m = (l + r) // 2 # Середина відрізка
        if x > array[m]:
            l = m + 1
        else:
            r = m

        alist = array[l:r + 1]
        print(alist)

    return array[r] == x


if __name__ == "__main__":
    a = [1, 2, 8, 13, 15, 17, 19, 20, 32, 42, 54, 92, 110, 222]
    print(binary_search(a, 2333))
