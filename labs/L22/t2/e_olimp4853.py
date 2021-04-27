
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

def bfs(g, s, f):
    n = len(g)

    q = Queue()
    q.enque(s)

    distances = [-1] * (n + 1)
    distances[s] = 0

    sources = [-1] * (n + 1)
    sources[s] = s

    while not q.empty():
        cur = q.deque()

        # додати в чергу всіх сусідів
        for neigbour in g[cur]:
            if distances[neigbour] == -1:
                q.enque(neigbour)
                distances[neigbour] = distances[cur] + 1
                sources[neigbour] = cur

    return distances[f], sources

dist, sources = bfs(g, a, b)
print(dist)

if dist != -1:
    cur = b
    path = []
    while cur != a:
        path.append(cur)
        cur = sources[cur]

    path.append(a)

    path = path[::-1]
    print(*path)


# if res == -1:
#     print(0)
# else:
#     print(res)
