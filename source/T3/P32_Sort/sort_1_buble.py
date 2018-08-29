def bubble_sort(array):
    """ Реалізує алгоритм сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            # Якщо наступний елемент менший за попередній
            if array[i] > array[i + 1]:
                # Міняємо місцями елементи, тобто
                # виштовхуємо більший елемент нагору
                array[i], array[i + 1] = array[i + 1], array[i]


if __name__ == "__main__":
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20, 44]
    bubble_sort(a)
    print(a)
