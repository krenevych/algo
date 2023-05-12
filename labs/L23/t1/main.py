# граф реалізовано через матрицю суміжності
graph = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, s = [int(el) for el in f_line.split()]
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        graph.append(row)


# # for debug - remove before submit
# print(f"vertices = {n}, selected vertex = {s}")
# for row in graph:
#     print(*row)


def dfs(start):
    global graph, visited, n
    visited.add(start) # помічаємо вершину як відвідану

    # запускати dfs для усіх сусідів вершини start які не були до цього відвідані
    for i in range(n):
        edge = graph[start-1][i] # є ребро між вершинами start i v, якщо edge == 1
        v = i + 1  # бо нумерація вершин у задачі з 1, а в списках у Python нумерація починається з нуля
        if edge != 0 and v not in visited:
            dfs(v)


visited = set()
dfs(s)

print(len(visited))
