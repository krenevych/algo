
"""
Реалізуйте швидкий алгоритм сортування QuickSort.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000

# Sorting time:  14.171875

def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    qsort(array, 0, len(array) - 1)


def qsort(array, a, b):
    # 1. Тривіальний випадок, коли [a, b] містить
    # лише один елемент, або порожній
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]  # опорний елемент
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
