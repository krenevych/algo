

g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, s, f = [int(el) for el in f_line.split()]
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        g.append(row)

# print(f"start = {s}")
# print(f"finish = {f}")
# for row in g:
#     print(*row)

class Queue:
    def __init__(self, size):
        self.q = [0] * size
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

def bfs():
    q = Queue(120)
    q.enque(s-1)

    visited = {s - 1: 0}
    while not q.empty():
        cur = q.deque()
        # print(cur + 1)
        for v in range(n):
            if g[cur][v] == 1 and v not in visited:
                q.enque(v)
                visited[v] = visited[cur] + 1

    if f - 1 in visited:
        return visited[f - 1]
    else:
        return 0


dist = bfs()
print(dist)
