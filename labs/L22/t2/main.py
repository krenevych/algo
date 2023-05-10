with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, m = [int(el) for el in f_line.split()]

    f_line = input_file.readline()
    a, b = [int(el) for el in f_line.split()]
    # граф реалізовано через список суміжності
    graph = {el: set() for el in range(1, n + 1)}
    for i in range(m):
        f_line = input_file.readline()
        cur, neig = [int(el) for el in f_line.split()]
        graph[cur].add(neig)
        graph[neig].add(cur)


# for debug - remove before submit
print(f"vertices = {n}, edges = {m}")
print(f"start = {a}, finish = {b}")
for v in graph:
    print(f"{v}: , {graph[v]}")
