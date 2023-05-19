# DEBUG = True
DEBUG = False

maze = []
with open("input.txt") as input_file:
    n = int(input_file.readline())
    if DEBUG: print(n)
    maze.append("*" * (n + 2))
    for i in range(n):
        row = input_file.readline().strip()
        maze.append("*" + row + "*")

    maze.append("*" * (n + 2))
    if DEBUG:
        for row in maze:
            print(row)

    start_row, start_col = map(int, input_file.readline().split())
    if DEBUG: print(start_row, start_col)

visited = []
# NON_VISITED = 0
# VISITED = 1

for i in range(len(maze)):
    row = [0] * len(maze[0])
    visited.append(row)

if DEBUG:
    for row in visited:
        print(row)

# рух дозволяється лише вгору, вправо, вниз, вліво
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# випадок, якщо можна також рухатися по діагоналі
# di = [-1, -1, 0, 1, 1,  1,  0, -1]
# dj = [ 0,  1 ,1, 1, 0, -1, -1, -1]
square_counter = 0


class Queue:
    def __init__(self, size):
        self.q = [(0, 0)] * size
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


def bfs(maze, visited, start_i, start_j):
    q = Queue(110) # розмір черги 101, оскільки за умовою задачі, лабіринт може мати не більше ніж 10 рядків та 10 стовпчиків
    q.enque((start_i, start_j))
    visited[start_i][start_j] = 1
    while not q.empty():
        i, j = q.deque()
        for k in range(len(di)):
            neig_i = i + di[k]
            neig_j = j + dj[k]
            if maze[neig_i][neig_j] != "*" and visited[neig_i][neig_j] == 0:
                visited[neig_i][neig_j] = 1
                q.enque((neig_i, neig_j))

bfs(maze, visited, start_row, start_col)

if DEBUG:
    print("After bfs")

for row in visited:
    if DEBUG: print(row)
    square_counter += sum(row)

print(square_counter)
