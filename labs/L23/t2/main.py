
def dfs(g, visited, start):
    for neighbour in g[start]:
        if neighbour not in visited:
            visited.add(neighbour)
            dfs(g, visited, neighbour)

g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, m = [int(el) for el in f_line.split()]
    for i in range(n + 1):
        neigbours = []
        g.append(neigbours)

    for i in range(m):
        f_line = input_file.readline()
        u, v = [int(el) for el in f_line.split()]
        g[u].append(v)
        g[v].append(u)


# print(g)

visited = set()
dfs(g, visited, 1)
print("YES" if len(visited) == n else "NO")


