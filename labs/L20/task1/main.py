from math import log2


class SegmentTree:
    def __init__(self, arr):
        k = len(arr)
        self.n = 1 << int(log2(k - 1) + 1)
        self.array = [0] * 2 * self.n

        # заповнюємо листки
        self.array[self.n: self.n + k] = arr

        # заповнюємо внутрішні вузли
        for i in range(self.n - 1, 0, -1):
            left = i * 2
            right = left + 1
            self.array[i] = self.array[left] + self.array[right]

        # print(self.array)

    def update(self, index, val):
        # print(f"update: {index} {val}")
        k = self.n + index
        self.array[k] = val
        k = k // 2
        while k > 0:
            left = k * 2
            right = left + 1
            self.array[k] = self.array[left] + self.array[right]
            k = k // 2

        # print(self.array)

    def suma(self, i, j):
        # return f"suma: {i}, {j}"
        res = 0
        l = i + self.n
        r = j + self.n
        while l <= r:
            if l % 2 == 1:  # l - права дитина
                res += self.array[l]
                l += 1
            if r % 2 == 0:  # r - ліва дитина
                res += self.array[r]
                r -= 1

            l = l // 2
            r = r // 2

        return res


if __name__ == '__main__':
    with open("input.txt") as input_file:
        n, q = map(int, input_file.readline().split())
        array = list(map(int, input_file.readline().split()))
        st = SegmentTree(array)
        for query in range(q):
            command = input_file.readline().split()
            if command[0] == "=":
                i, d = map(int, (command[1], command[2]))
                st.update(i - 1, d)  # елемент з індексом i магічно стає рівним d.
            elif command[0] == "?":
                f, t = map(int, (command[1], command[2]))
                print(st.suma(f - 1, t - 1))  # сума усіх чисел у масиві з індексами від f до t?
