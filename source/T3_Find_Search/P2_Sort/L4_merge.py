
def merge_sort(array):
    """ Реалізує алгоритм сортування злиттям

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


if __name__ == "__main__":
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    merge_sort(a)
    print(a)
