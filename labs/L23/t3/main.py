def dfs(g, visited, start):
    n = len(g)
    for neighbour in range(n):
        if g[start][neighbour] != 0 and neighbour not in visited:
            visited.add(neighbour)
            dfs(g, visited, neighbour)


g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n = int(f_line)
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        g.append(row)

visited = set()
current_connectivity_component = 0
for i in range(n):
    if i not in visited:
        current_connectivity_component += 1
        dfs(g, visited, i)

print(current_connectivity_component)
