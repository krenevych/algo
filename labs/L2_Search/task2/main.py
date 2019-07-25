from random import randint
import numpy
import user

N = 100000  # Кількість елементів масиву


def testBsearch():
    arr = numpy.random.randint(0, 100000, N)
    arr.sort()

    errors = 0
    for i in range(N):
        v = randint(0, 100000)
        r = user.bsearch_leftmost(arr, v)

        if (r != 0 and arr[r - 1] >= v) or (r != N and arr[r] < v):
            errors += 1

    print("bsearch errors:",  errors)


if __name__ == "__main__":
    testBsearch()

