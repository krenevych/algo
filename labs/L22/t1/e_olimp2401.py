
class Queue:
    def __init__(self):
        self.q = [0] * 200
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

g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, s, f = [int(el) for el in f_line.split()]
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        g.append(row)

def bfs(g, s, f):
    n = len(g)

    q = Queue()
    q.enque(s)

    distances = [-1] * n
    distances[s] = 0

    while not q.empty():
        cur = q.deque()

        # додати в чергу всіх сусідів
        for i in range(n):
            if g[cur][i] == 1 and distances[i] == -1:
                q.enque(i)
                distances[i] = distances[cur] + 1

    return distances[f]


res = bfs(g, s - 1, f - 1)
if res == -1:
    print(0)
else:
    print(res)
