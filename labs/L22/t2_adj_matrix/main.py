

g = []
with open("input.txt") as input_file:
    f_line = input_file.readline()
    n, m = [int(el) for el in f_line.split()]
    print(n, m)  # FIXME: for debug
    f_line = input_file.readline()
    a, b = [int(el) for el in f_line.split()]
    print(a, b)   # FIXME: for debug
    for i in range(m):
        f_line = input_file.readline()
        edge = [int(el) for el in f_line.split()]
        print(edge) # FIXME: for debug

