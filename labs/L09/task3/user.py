"""
Проведіть аналіз швидкодії реалізованих алгоритмів сортування
для різних типів та розмірів масивів (не відсортований масив
згенерований випадковим чином, масив відсортований за зростанням,
масив відсортований за спаданням елементів).
"""

N = 10_000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for edge in range(n - 1, 0, -1):
        for i in range(edge):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for edge in range(n - 1, 0, -1):
        isSorted = True
        for i in range(edge):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        if isSorted: break


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for edge in range(n - 1, 0, -1):
        max_pos = 0
        for i in range(1, edge + 1):
            if array[i] > array[max_pos]:
                max_pos = i

        array[edge], array[max_pos] = array[max_pos], array[edge]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for index in range(1, n):

        currentValue = array[index] # запам’ятовуємо елемент, що необхідно вставити
        position = index            # та його позицію

        # пошук позиції для вставки поточного елемента
        while position > 0:
            if array[position - 1] > currentValue:
                # зсув елементу масиву вправо
                array[position] = array[position - 1]
            else:
                # знайдено позицію
                break
            position -= 1

        # Вставка поточного елемента у знайдену позицію
        array[position] = currentValue


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    # print("Splitting ", array)
    if len(array) > 1:
        # Розбиття списку навпіл
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        # Рекурсивний виклик сортування
        # для кожної з половин
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # Злиття двох відсортованих списків
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1


def qsort(array, a, b):
    if a >= b: return  # якщо фрагмент масиву, що треба відсортувати складається з одного елементу або порожній, то фрагмент вже відсортований

    l = a
    r = b
    pivot = array[l + (r - l) // 2]
    while True:
        while array[l] < pivot: l += 1
        while array[r] > pivot: r -= 1
        if l >= r: break
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1

    qsort(array, a, r)
    qsort(array, r + 1, b)

def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    qsort(array, 0, len(array) - 1)

