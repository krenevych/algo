

g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, m = [int(el) for el in f_line.split()]
    for v in range(n + 1):
        g.append(set())
    # print(n, m)  # FIXME: for debug
    f_line = input_file.readline()
    a, b = [int(el) for el in f_line.split()]
    # print("a, b = ", a, b)   # FIXME: for debug
    for i in range(m):
        f_line = input_file.readline()
        edge_begin, edge_end = [int(el) for el in f_line.split()]

        # print(edge) # FIXME: for debug
        g[edge_begin].add(edge_end)
        g[edge_end].add(edge_begin)

    # print(g)


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
    q = Queue(100_005)
    q.enque(a)

    visited = {a: 0}
    sources = {a: None}
    while not q.empty():
        cur = q.deque()

        for neig in g[cur]:
            if neig not in visited:
                q.enque(neig)
                visited[neig] = visited[cur] + 1
                sources[neig] = cur

    # print("visited: ", visited)
    # print("sources: ", sources)

    if b not in visited:
        print(-1)
        return

    cur = b
    way = [cur]
    # print(cur, " <- ", end="")
    while cur != a:
        cur = sources[cur]
        # print(cur, " <- ", end="")
        way.append(cur)
    # print()

    print(visited[b])
    print(*way[::-1])


bfs()


