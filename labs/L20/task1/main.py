from math import log2


class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = 1 << (int(log2(k - 1)) + 1)
        self.n = n
        self.array = 2 * n * [0]
        self.array[n: k] = array  # заповнюємо листки

        # заповнюємо внутнішні вузли
        for i in range(n - 1, 0, -1):
            left = 2 * i
            right = left + 1
            self.array[i] = self.array[left] + self.array[right]

    def update(self, i, d):
        i += self.n
        self.array[i] = d
        while i > 1:
            parent = i // 2
            left = 2 * parent
            right = left + 1
            self.array[parent] = self.array[left] + self.array[right]
            i = parent

    def suma(self, f, t):
        left = f + self.n
        right = t + self.n
        res = 0

        while left <= right:
            if left % 2 == 1: # left права дитина
                res += self.array[left]
            if right % 2 == 0: # right ліва дитина
                res += self.array[right]

            left = (left + 1) // 2  # переходимо на попередній рівень дерева
            right = (right - 1) // 2  # переходимо на попередній рівень дерева

        return res






with open("input.txt") as input_file:
    n, q = map(int, input_file.readline().split())
    array = list(map(int, input_file.readline().split()))
    st = SegmentTree(array)
    for query in range(q):
        command = input_file.readline().split()
        if command[0] == "=":
            i, d = map(int, (command[1], command[2]))
            st.update(i - 1, d) # елемент з індексом i магічно стає рівним d.
        elif command[0] == "?":
            f, t = map(int, (command[1], command[2]))
            print(st.suma(f - 1, t - 1)) # сума усіх чисел у масиві з індексами від f до t?
