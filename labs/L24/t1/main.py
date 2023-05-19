maze = []
with open("input.txt") as input_file:
    n = int(input_file.readline())
    # print(n)
    maze.append("*" * (n + 2))
    for i in range(n):
        row = input_file.readline().strip()
        maze.append("*" + row + "*")
        # print(row)
    maze.append("*" * (n + 2))
    # for row in maze:
    #     print(row)

    start_row, start_col = map(int, input_file.readline().split())
    # print(start_row, start_col)

visited = []
# NON_VISITED = 0
# VISITED = 1

for i in range(len(maze)):
    row = [0] * len(maze[0])
    visited.append(row)

# for row in visited:
#     print(row)

# рух дозволяється лише вгору, вправо, вниз, вліво
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# випадок, якщо можна також рухатися по діагоналі
# di = [-1, -1, 0, 1, 1,  1,  0, -1]
# dj = [ 0,  1 ,1, 1, 0, -1, -1, -1]
square_counter = 0
def dfs(maze, visited, start_i, start_j):
    visited[start_i][start_j] = 1
    global square_counter
    square_counter += 1

    # запускаємо dfs для всіх сусідів клітини start_i, start_j
    for k in range(len(di)):
        neig_i = start_i + di[k]  # рядок
        neig_j = start_j + dj[k]  # стовпчик
        # якщо сусідня клітина не стінка і вона не була відвідана
        if maze[neig_i][neig_j] != "*" and visited[neig_i][neig_j] == 0:
            dfs(maze, visited, neig_i, neig_j)


dfs(maze, visited, start_row, start_col)

# print("After dfs")
# for row in visited:
#     square_counter += sum(row)
#     print(row)

print(square_counter)
