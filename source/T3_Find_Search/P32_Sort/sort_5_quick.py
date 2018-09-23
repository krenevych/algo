def quick_sort(array):
    """ Реалізує алгоритм швидкого сортування

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(array, first, last):
    """ Допоміжний рекурсивний метод,
        що реалізує сортування фрагменту списку обмеженого заданими позиціями

    :param array: Масив (список однотипових елементів)
    :param first: Ліва межа списку
    :param last: Права межа списку
    :return: None
    """
    if first < last:
        # Визанчення точки розбиття спику
        splitpoint = partition(array, first, last)
        # Рекурсивний виклик функції швидкого сортування
        # для отриманих частин списку
        quick_sort_helper(array, first, splitpoint - 1)
        quick_sort_helper(array, splitpoint + 1, last)

def partition(array, first, last):
    """ Визначає точку розбиття списку

    :param array: Масив (список однотипових елементів)
    :param first: Ліва межа списку
    :param last: Права межа списку
    :return: Позицію розбиття списку
    """
    pivot = array[first]
    left = first + 1
    right = last
    done = False
    while not done:
        # Рухаємося зліва на право,
        # поки не знайдемо елемент, що більший за опорний
        while left <= right and array[left] <= pivot:
            left += 1

        # Рухаємося справа на ліво,
        # поки не знайдемо елемент, що менший за опорний
        while array[right] >= pivot and right >= left:
            right -= 1

        # Якщо індекс правого елемента менший за індекс лівого
        if right < left:
            # то розбиття списку завершено
            done = True
        else:
            # міняємо знайдений елементи місцями
            array[left], array[right] = array[right], array[left]

        # print(array)
    # ставимо опорний елемент на його позицію
    array[first], array[right] = array[right], array[first]
    return right


if __name__ == "__main__":
    a = [56, 12, 66, 20, 33, 95, 32, 13, 10]
    quick_sort(a)
    print(a)
