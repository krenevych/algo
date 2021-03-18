"""
Проведіть аналіз швидкодії реалізованих алгоритмів сортування
для різних типів та розмірів масивів (не відсортований масив
згенерований випадковим чином, масив відсортований за зростанням,
масив відсортований за спаданням елементів).
"""

N = 1000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for pasNum in range(n - 1, 0, -1):
        for i in range(pasNum):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        isSorted = True
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                isSorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        if isSorted:
            break


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        ind_max = 0
        for i in range(1, pass_num + 1):
            if array[i] > array[ind_max]:
                ind_max = i

        array[ind_max], array[pass_num] = array[pass_num], array[ind_max]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for index in range(1, n):
        current = array[index]
        for i in range(index - 1, -1, -1):
            if array[i] > current:
                array[i + 1] = array[i]
            else:
                array[i + 1] = current
                break


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) <= 1:
        return
        # 2. розбиваємо масив на дві половини і здійснюємо
        #    рекурсивний вклик сортування для кожної половини.
    m = len(array) // 2
    left = array[:m]
    right = array[m:]
    merge_sort(left)
    merge_sort(right)
    # 3. зливаємо дві відсортовані половини у один
    #    відсортований масив
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):  # якщо залишилися елементи
        # у лівому масиві
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):  # якщо залишилися елементи
        # у правому масиві
        array[k] = right[j]
        j += 1
        k += 1


def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    qsort(array, 0, len(array) - 1)


def qsort(array, a, b):
    # 1. Тривіальний випадок, коли [a, b] містить
    # лише один елемент, або порожній
    if a >= b:
        return

    # pivot = array[a + (b - a) // 2]  # опорний елемент
    pivot = array[a]  # опорний елемент
    # 2. Розбиваємо вхідний масив на дві частини так,
    # щоб ліва частина містили елементи масиву,
    # що менші або рівні за опорний,
    # а права - більші або рівні за опорний
    left = a
    right = b

    while True:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    qsort(array, a, right)
    qsort(array, right + 1, b)

