def linear_search(array, x):
    """ Лінійний пошук у масиві

    :param array: Список елементів
    :param x: Шуканий елемент
    :return: True, якщо шуканий елемент знайдено
    """

    for el in array:
        if el == x:
            return True
    return False


if __name__ == "__main__":
    a = [1, 2, 8, 13, 15, 17, 19, 20, 32, 42, 54, 92, 110, 222]
    print(linear_search(a, 2333))
