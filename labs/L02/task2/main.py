from random import randint
from time import process_time

import numpy
import user


def test(TestName, N, M):
    arr = numpy.random.randint(0, M, N)
    arr.sort()

    errors = 0

    dt = process_time()
    for i in range(N):
        v = randint(0, M)
        r = user.bsearch_leftmost(arr, v)

        if (r != 0 and arr[r - 1] >= v) or (r != N and arr[r] < v):
            errors += 1
    dt = process_time() - dt
    print(TestName, " Errors: %6d" % errors, " Running time: %2.5f" % dt)


if __name__ == "__main__":
    test("TEST #1", 100000, 100000)
    test("TEST #2", 100, 100000)
    test("TEST #3", 100000, 100)
