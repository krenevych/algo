min_value = 100500
matrix_value = []


def calc(value, worker, free: set):
    global min_value

    if min_value < value:
        return

    if len(free) == 0:
        if min_value > value:
            min_value = value

    for work in free:
        rest = set(free)
        rest.remove(work)

        new_value = value + matrix_value[worker][work]
        calc(new_value, worker + 1, rest)


with open("input.txt") as f:
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        row = list(map(int, line.split()))
        matrix_value.append(row)

    min_value = 100500
    start_free = set(range(n))
    calc(0, 0, start_free)
    print(min_value)
