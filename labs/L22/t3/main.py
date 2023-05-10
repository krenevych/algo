
# граф реалізовано через матрицю суміжності
graph = []
with open("input.txt") as input_file:
    n = int(input_file.readline())
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        graph.append(row)

# for debug - remove before submit
print(f"vertices = {n}")
for row in graph:
    print(*row)
