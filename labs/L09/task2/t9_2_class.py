MAX_MULT = 0


def divide(mult, n, parts):
    global MAX_MULT
    cur_mult = mult * int(n)
    if cur_mult < MAX_MULT: return
    if parts == 1:
        if cur_mult > MAX_MULT:
            MAX_MULT = cur_mult
        return

    for divide_pos in range(1, len(n) - parts + 2):
        divide(mult * int(n[:divide_pos]), n[divide_pos:], parts - 1)


with open("input.txt") as f:
    for line in f:
        n, m = line.split()
        MAX_MULT = 0
        divide(1, n, int(m))
        print(MAX_MULT)