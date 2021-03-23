
operation = {"+", "-", "*"}
def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b

IS_POSSIBLE = False
def permut(orig, cur):
    global IS_POSSIBLE
    if IS_POSSIBLE:
        return

    if len(orig) == 0:
        # 1 + 2 + 3 + 4 + 5
        for op1 in operation:
            for op2 in operation:
                for op3 in operation:
                    for op4 in operation:
                        res = calc(cur[0], cur[1], op1)
                        res = calc(res, cur[2], op2)
                        res = calc(res, cur[3], op3)
                        res = calc(res, cur[4], op4)
                        if res == 23:
                            IS_POSSIBLE = True

        return

    for el in orig:
        new_cur = cur[:]
        new_orig = orig[:]

        new_cur.append(el)
        new_orig.remove(el)
        permut(new_orig, new_cur)





with open("input.txt") as f:
    for line in f:
        lst = list(map(int, line.split()))
        if lst[0] == lst[1] == lst[2] == lst[3] == lst[4] == 0:
            break

        IS_POSSIBLE = False
        permut(lst, [])
        if IS_POSSIBLE:
            print("Possible")
        else:
            print("Impossible")
