# -*- coding: utf-8 -*-

def qsort(array, a, b):
    """ Швидке сортування масиву

    :param array: масив
    :param a: ліва межа сортування
    :param b: права межа сортування
    """

    if a >= b:
        return

    pivot = array[a + (b - a) // 2]  # опорний елемент
    left = a                         # лівий маркер
    right = b                        # правий маркер
    while True:
        while array[left] < pivot:   # Рухаємося зліва на право, поки не знайдемо
                                     # елемент, що більший або рівний за опорний
            left += 1

        while pivot < array[right]:  # Рухаємося справа на ліво, поки не знайдемо
                                     # елемент,що менший або рівний за опорний
            right -= 1

        if left >= right:  # маркери вказують на один і той де елемент або
                           # лівий маркер займає позицію праворуч від правого
            break

        array[left], array[right] = array[right], array[left]  # міняємо місцями елементи
        left += 1          #  зміщуємо лівий маркер вправо
        right -= 1         #  зміщуємо правий маркер вліво

    #  рекурсивно повторюємо процедуру для лівого та правого підсписків
    qsort(array, a, right)
    qsort(array, right + 1, b)


if __name__ == "__main__":
    a = [56, 12, 66, 20, 33, 95, 32, 13, 10]
    qsort(a, 0, len(a) - 1)
    print(a)