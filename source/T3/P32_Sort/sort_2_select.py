def selection_sort(array):
    """ Реалізує алгоритм сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        # реалізуємо пошук найбільшого елементу
        maxpos = 0
        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j

        # Міняємо місцями поточний і найбільший елемент
        array[i], array[maxpos] = array[maxpos], array[i]


if __name__ == "__main__":
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    selection_sort(a)
    print(a)