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


def bfs(maze, si, sj):
    distances = []
    n = len(maze)
    for i in range(n):
        row = [-1] * n
        distances.append(row)

    print()
    print()
    for r in distances:
        print(r)

    qi = Queue(100)
    qj = Queue(100)

    qi.enque(si)
    qj.enque(sj)
    distances[si][sj] = 0

    while not qi.empty():
        curi = qi.deque()
        curj = qj.deque()
        #     проходимося по сусідах
        for k in range(len(di)):
            ni = curi + di[k]  # координата рядка сусіда
            nj = curj + dj[k]  # координата стовпчика сусіда
            if maze[ni][nj] == "." and distances[ni][nj] == -1:
                distances[ni][nj] = distances[curi][curj] + 1
                qi.enque(ni)
                qj.enque(nj)

    print()
    print()
    for r in distances:
        for el in r:
            print(f"{el:4}", end="")
        print()


di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

# di = [-1, 0, 1, 0, -1,  1, 1, -1]
# dj = [0, -1, 0, 1, -1, -1, 1,  1]

maze = []
with open("input.txt") as input_file:
    n = int(input_file.readline())
    fline = "*" * (n + 2)
    lline = "*" * (n + 2)
    maze.append(fline)
    for i in range(n):
        row = "*" + input_file.readline().rstrip() + "*"
        maze.append(row)
    maze.append(lline)
    si, sj = map(int, input_file.readline().split())

    bfs(maze, si, sj)
