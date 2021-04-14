from math import log2


class SegmentTree:

    def __init__(self, array):
        """ Конструктор - створює бінарне дерево пошуку

        :param array: Вхідний масив елементів
        """
        k = len(array)                   # кількість елементів у масиві даних
        n = (1 << int(log2(k - 1)) + 1)  # доводимо розмірність масиву до степені 2
        self.mItems = 2 * n * [0]        # масив для збереження вузлів дерева

        # записуємо дані вхідного масиму у листки дерева
        for i in range(k):
            self.mItems[n + i] = array[i]

        # записуємо дані для внутнішніх вузлів дерева
        for i in range(n - 1, 0, -1):
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]

        self.mSize = n   # запам'ятовуємо розмірність масиву

    def update(self, pos, x):
        """ Заміняє значення ключа у вхідному масиві

        :param pos: позиція елемента вхідного масиву, що потрібно замінити
        :param x:   нове значення
        """

        pos += self.mSize
        self.mItems[pos] = x  # Змінюємо значення у листі

        # перераховуємо значення у внутрішних вузлах
        i = pos // 2  # Позиція батьківського вузла
        while i > 0:
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]
            i //= 2

    def sum(self, left, right):
        """ Сума елементів відрізку від left до right вхідного масиву

        :param left: ліва межа відрізку
        :param right: права межа відрізку
        :return:
        """
        left += self.mSize
        right += self.mSize

        res = 0

        while left <= right:
            if left % 2 == 1:   # якщо  left - правий син свого батька
                res += self.mItems[left]
            if right % 2 == 0:  # якщо right - лівий син свого батька
                res += self.mItems[right]

            # піднімаємося у дереві на рівень вище
            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

    def __setitem__(self, key, value):
        """ Перевизначення квадратних дужок (на запис) для класу SegmentTree """
        self.update(key, value)

    def __getitem__(self, item):
        """ Перевизначення квадратних дужок (на читання) для класу SegmentTree """
        item += self.mSize
        return self.mItems[item]

    def __call__(self, left, right):
        """ Перевизначення круглих дужок для класу SegmentTree """
        return self.sum(left, right)


if __name__ == "__main__":
    a = [2, 7, 6, 4, 1, 3, 5, 8]
    segTree = SegmentTree(a)

    S = segTree(0, 7)
    print(S)

    segTree[3] = 0
    S = segTree(0, 7)
    print(S)
