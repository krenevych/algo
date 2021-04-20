def siftDown(array, start, size):
    while 2 * start + 1 < size:
        left = 2 * start + 1
        right = left + 1

        if right >= size:
            maxChild = left
        elif array[left] > array[right]:
            maxChild = left
        else:
            maxChild = right

        if array[start] < array[maxChild]:
            array[start], array[maxChild] = array[maxChild], array[start]
        else:
            break

        start = maxChild


def heapsort(array):
    size = len(array)
    # відновлюємо у масиві стуруктуру бінарної купи
    for i in range(size // 2, -1, -1):
        siftDown(array, i, size)

    # виштовхуємо у кінець найбільші елементи купи
    for range_of_heap in range(size - 1, 0, -1):
        print(*array)
        array[0], array[range_of_heap] = array[range_of_heap], array[0]
        print(*array)
        siftDown(array, 0, range_of_heap)


with open("input.txt") as f:
    array = list(map(int, f.readline().split()))
    heapsort(array)
    print(*array)