from math import log2


class SegmentTree:
    def __init__(self, arr):
        print(arr)

    def update(self, index, val):
        print(f"update: {index} {val}")

    def suma(self, i, j):
        return f"suma: {i}, {j}"


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
