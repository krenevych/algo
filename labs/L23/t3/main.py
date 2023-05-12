# граф реалізовано через матрицю суміжності
graph = []
with open("input.txt") as input_file:
    n = int(input_file.readline())
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        graph.append(row)

# for debug - remove before submit
# print(f"vertices = {n}")
# for row in graph:
#     print(*row)


def dfs(start, marker_component):
    global graph, visited, n
    visited[start] = marker_component
    for i in range(n):
        if graph[start][i] != 0 and i not in visited:
            dfs(i, marker_component)


visited = {}  # вершина: номер компоненти зв'язності, до якої вона належить
component_marker = 0
for i in range(n):
    if i not in visited:
        component_marker += 1
        dfs(i, component_marker)

# print(visited)
print(component_marker)
