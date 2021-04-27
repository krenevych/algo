
with open("input.txt") as infile:
    n = int(infile.readline())
    edges = 0  # кількість ребер
    for i in range(n):
        row = list(map(int, infile.readline().split()))
        for j in range(n):
            if row[j] > 0:  # знайшли ребро
                edges += 1

    print(edges)

