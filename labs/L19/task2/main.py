def siftDown(array, cur, size):
    while 2 * cur + 1 < size:
        maxChild = getMaxChild(array, cur, size)
        if array[maxChild] > array[cur]:
            swap(array, maxChild, cur)
            cur = maxChild
        else:
            break


def getMaxChild(arr, cur, size):
    left = 2 * cur + 1
    right = left + 1
    if right >= size:
        return left

    return left if arr[left] > arr[right] else right


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapsort(array):
    # відновлюємо у масиві стуруктуру бінарної купи
    # TODO:

    # виштовхуємо у кінець найбільші елементи купи
    # TODO:

    pass


if __name__ == '__main__':
    with open("input.txt") as f:
        array = list(map(int, f.readline().split()))
        heapsort(array)
        print(*array)
