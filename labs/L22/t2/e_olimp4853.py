
QUEUE_SIZE = 100000
class Queue:
    def __init__(self):
        self.q = [0] * QUEUE_SIZE
        self.b = 0
        self.e = 0

    def enque(self, item):
        self.q[self.e] = item
        self.e += 1

    def deque(self):
        item = self.q[self.b]
        self.b += 1
        return item

    def empty(self):
        return self.b == self.e


with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, m = [int(el) for el in f_line.split()]

    f_line = input_file.readline()
    a, b = [int(el) for el in f_line.split()]

    g = {el : set() for el in range(1, n + 1)}
    for i in range(m):
        f_line = input_file.readline()
        cur, neig  = [int(el) for el in f_line.split()]
        g[cur].add(neig)
        g[neig].add(cur)

