def heapSort(array):
    """ Пірамідальне сортування вхідного масиву
    :param array: вхідний масив даних
    """

    size = len(array)
    # Відновлення стутуктури двійкової купи для вхідного масиву даних
    # Для всіх внутрішніх вузлів дерева двійкової купи
    # (для вузлів з індексами [0, size / 2] )
    for i in range(size // 2 - 1, -1, -1):
        siftDown(array, i, size)  # здійснюємо просіювання вниз

    # Для всіх внутрішніх вузлів дерева двійкової купи
    for i in range(size - 1, 0, -1):
        # Преставляємо найбільший елемент у кінець
        array[0], array[i] = array[i], array[0]
        # тепер частина масиву з індексами [i, size - 1] відсортована
        # Відновлюємо структуру двійкової купи для частини масиву [0, i - 1]
        siftDown(array, 0, i)  # просіюванням елементу з індексом 0 вниз


def siftDown(array, start, end):
    """ Функція просіювання елементів двійкової купи вниз
    Здійснює просіювання елементів двійкової купи
    у діапазоні [start, end - 1] так, що найбільший елемент
    найбільший елемент опиняється у позиції start

    :param array: Вхідний масив, що моделює двійкову купу
    :param end:   Розмір двійкової купи
    :param start: Початковий індекс
    """
    while True:

        # Визначаємо лівого та правого синів поточного вузла
        # Індекси масиву починаються від нуля, тому
        left = start * 2 + 1
        right = left + 1

        largest = start
        if left < end and array[left] > array[largest]:
            largest = left
        if right < end and array[right] > array[largest]:
            largest = right
        if largest == start:
            break

        array[start], array[largest] = array[largest], array[start]
        start = largest
