def dod(a, b):
    return a + b


def mno(a, b):
    return a * b


def vid(a, b):
    return a - b


operators = [dod, vid, mno]


def check23(d):
    res = d[0]
    for op1 in operators:
        res1 = op1(res, d[1])
        for op2 in operators:
            res2 = op2(res1, d[2])
            for op3 in operators:
                res3 = op3(res2, d[3])
                for op4 in operators:
                    res4 = op4(res3, d[4])

                    # print(op1, op2, op3, op4)
                    # print(res4)
                    if res4 == 23:
                        return True

    return False


if __name__ == '__main__':
    with(open("input.txt") as f):
        for line in f:
            digits = [int(el) for el in line.split()]
            print(digits)
            if sum(digits) != 0:
                if check23(digits):
                    print("Possible")
                else:
                    print("Impossible")
