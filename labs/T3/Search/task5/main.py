import math

import user
eps = 0.0000000001

def case1():
    f = lambda x: math.tan(x) - 2.0 * x
    a = 0.5
    b = 1.5
    c = 0
    r = user.solve(f, c, a, b)
    print("Case 1: ", abs(c - f(r)) <= eps)


def case2():
    f = math.sin
    a = 0
    b = 1.5
    c = 0.5
    r = user.solve(f, c, a, b)
    print("Case 2: ", abs(c - f(r)) <= eps)


def case3():
    f = math.cos
    a = 0
    b = 1.5
    c = 0.5
    r = user.solve_decreasing(f, c, a, b)
    print("Case 3: ", abs(c - f(r)) <= eps)


def case4():
    f = lambda x: 4 - x ** 2
    a = 0.4
    b = 1.9
    c = 2.7
    r = user.solve_decreasing(f, c, a, b)
    print("Case 4: ", abs(c - f(r)) <= eps)


def case5():
    f = lambda x: x ** 3
    a = 0.4
    b = 9.9
    c = 7.345
    r = user.solve(f, c, a, b)
    print("Case 5: ", abs(c - f(r)) <= eps)


if __name__ == "__main__":
    case1()
    case2()
    case3()
    case4()
    case5()
