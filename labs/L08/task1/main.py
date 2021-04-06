import time

import numpy
import user

def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            errors += 1

    print("Errors:       ", errors)


def testSort():

    s = numpy.random.randint(0, 100000, user.N)
    t = time.process_time()
    user.sort(s)
    dt = time.process_time() - t
    print('Sorting time: ', dt)
    checkResult(s)


if __name__ == "__main__":
    testSort()






