from math import log2


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = (1 << int(log2(k - 1)) + 1)

        self.mItems = 2 * n * [0]

        for i in range(k):
            self.mItems[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]

        self.mSize = n

    def update(self, pos, x):
        pos += self.mSize
        self.mItems[pos] = x

        i = pos // 2  # Позиція батьківського вузла
        while i > 0:
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]
            i //= 2

    def sum(self, left, right):
        left += self.mSize
        right += self.mSize

        res = 0

        while left <= right:
            if left % 2 == 1:  # якщо left - правий син свого батька
                res += self.mItems[left]
            if right % 2 == 0:  # якщо right - лівий син свого батька
                res += self.mItems[right]

            # піднімаємося у дереві на рівень вище
            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

    def __setitem__(self, key, value):
        self.update(key, value)

    def __getitem__(self, item):
        item += self.mSize
        return self.mItems[item]

    def __call__(self, left, right):
        return self.sum(left, right)


if __name__ == "__main__":
    a = [2, 7, 6, 4, 1, 3, 5, 8]
    segTree = SegmentTree(a)

    S = segTree(0, 7)
    print(S)

    segTree[3] = 0
    S = segTree(0, 7)
    print(S)
