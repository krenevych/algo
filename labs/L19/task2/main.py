def siftDown(array, cur, size):
    while 2 * cur + 1 < size:
        maxChild = getMaxChild(array, cur)

        if array[maxChild] > array[cur]:
            array[cur], array[maxChild] = array[maxChild], array[cur]
            cur = maxChild
        else:
            break


def getMaxChild(array, cur):
    size = len(array)
    left = 2 * cur + 1
    right = left + 1
    if right >= size:
        return left

    return left if array[left] > array[right] else right


def heapsort(array):
    size = len(array) - 1
    for cur in range(size // 2 - 1, -1, -1):
        siftDown(array, cur, size)

    # TODO: реалізувати другу частину алгоритму - виштовхування найбільших елементів у кінець масиву


if __name__ == '__main__':
    with open("input.txt") as f:
        array = list(map(int, f.readline().split()))
        heapsort(array)
        print(*array)
