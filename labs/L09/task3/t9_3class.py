
def assign(cur_value, works, worker):
    global MIN_VALUE
    if cur_value > MIN_VALUE:
        return

    if len(works) == 0:
        if cur_value < MIN_VALUE:
            MIN_VALUE = cur_value
        return

    for work in works:
        new_works = set(works)
        new_works.remove(work)
        assign(cur_value + values[worker][work], new_works, worker + 1)


with open("input.txt") as f:
    n = int(f.readline())
    values = []
    for i in range(n):
        row = list(map(int, f.readline().split()))
        values.append(row)


    MIN_VALUE = 100500
    assign(0, set(range(n)), 0)
    print(MIN_VALUE)