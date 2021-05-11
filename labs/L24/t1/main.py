def dfs(maze, si, sj):
    visited = []
    n = len(maze)
    for i in range(n):
        row = [0] * n
        visited.append(row)

    __dfs_helper(maze, si, sj, visited)

    # suma = 0
    # for r in visited:
    #     # print(r)
    #     for el in r:
    #         suma += el
    #
    # return suma


di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]


# di = [-1, 0, 1, 0, -1,  1, 1, -1]
# dj = [0, -1, 0, 1, -1, -1, 1,  1]

def __dfs_helper(maze, si, sj, visited):
    visited[si][sj] = 1
    global square
    square += 1
    #     запускаємо DFS для усіх сусідів поточної клітини
    for k in range(len(di)):
        ni = si + di[k]  # координата рядка сусіда
        nj = sj + dj[k]  # координата стовпчика сусіда
        if maze[ni][nj] == "." and visited[ni][nj] != 1:
            __dfs_helper(maze, ni, nj, visited)


maze = []
square = 0
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

    # for r in maze:
    #     print(r)
    # print(si, sj)

    dfs(maze, si, sj)
    print(square)
