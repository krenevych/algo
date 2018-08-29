def insertion_sort(array):
    """ Реалізує алгоритм сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for index in range(1, n):

        currentValue = array[index]
        position = index

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


if __name__ == "__main__":
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    insertion_sort(a)
    print(a)
