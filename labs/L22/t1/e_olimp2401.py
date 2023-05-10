

g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, s, f = [int(el) for el in f_line.split()]
    for i in range(n):
        f_line = input_file.readline()
        row = [int(el) for el in f_line.split()]
        g.append(row)

print(f"start = {s}")
print(f"finish = {f}")
for row in g:
    print(*row)
