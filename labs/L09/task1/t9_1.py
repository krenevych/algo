def calc(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b


operators = ["+", "-", "*"]

IS_POSSIBLE = False
def check(d):
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                for op4 in operators:
                    res = calc(d[0], d[1], op1)
                    res = calc(res, d[2], op2)
                    res = calc(res, d[3], op3)
                    res = calc(res, d[4], op4)
                    if res == 23:
                        global IS_POSSIBLE
                        IS_POSSIBLE = True


def permut(orig, permutated):
    global IS_POSSIBLE
    if IS_POSSIBLE:
        return

    if len(orig) == 0:
        check(permutated)
        return

    el = orig[-1]
    new_orig = orig[:-1]
    for i in range(len(permutated) + 1):
        new_permutated:list = permutated[:]
        new_permutated.insert(i, el)
        permut(new_orig, new_permutated)




with open("input.txt") as f:
    while True:
        line = f.readline()
        d = list(map(int, line.split()))
        if d[0] == d[1] == d[2] == d[3] == d[4] == 0:
            break

        # a + b + c + d + e

        IS_POSSIBLE = False
        permut(d, [])

        if IS_POSSIBLE:
            print("Possible")
        else:
            print("Impossible")
