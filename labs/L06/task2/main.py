import time
import user
from random import randint

DEBUG = False
N_MAXKEY = 10000000
TIME_TEST_LIMIT = 40_000_000  # 40 msec
VERIFICATION_THRESHOLD = 70

_array = {}
_deleted = set()


def generate_pairs(fname, N):
    f_out = open(fname, "w", encoding='utf-8')
    for i in range(N):
        key = randint(0, N_MAXKEY)
        chars = randint(2, 50)
        value = ""
        for j in range(chars):
            ch = randint(0, 25)
            value += chr(ord('a') + ch)
        word = str(key) + "=" + value
        print(word, file=f_out, end="\n")
    f_out.close()


def readData(fname):
    with open(fname, encoding='utf-8') as f_in:
        for line in f_in:
            pair = line.strip().split('=')
            key, value = int(pair[0]), pair[1]
            add(key, value)


def add(key, value):
    global _array, _deleted
    _array[key] = value
    t = time.time_ns()
    user.set(key, value)
    dt = time.time_ns() - t
    if key in _deleted:
        _deleted.remove(key)

    if DEBUG and dt >= TIME_TEST_LIMIT:
        print(f"ALARM add: dt >= TIME_TEST_LIMIT, dt = {dt}")

    return dt < TIME_TEST_LIMIT


def delete():
    global _array, _deleted
    size = len(_array)

    num = randint(0, size - 1)
    key = list(_array)[num]

    del _array[key]
    _deleted.add(key)

    t = time.time_ns()
    user.delete(key)
    dt = time.time_ns() - t

    if DEBUG and dt >= TIME_TEST_LIMIT:
        print(f"ALARM delete: dt >= TIME_TEST_LIMIT, dt = {dt}")

    return dt < TIME_TEST_LIMIT


def checkFind():
    global _array, _deleted
    size = len(_array)
    num = randint(0, size - 1)
    key = list(_array)[num]

    val = _array[key]

    t = time.time_ns()
    user_val = user.get(key)
    dt = time.time_ns() - t

    if DEBUG and dt >= TIME_TEST_LIMIT:
        print(f"ALARM checkFind: dt >= TIME_TEST_LIMIT, dt = {dt}")

    if DEBUG and user_val != val:
        print("ALARM checkFind: user_val != val")

    return user_val == val and dt < TIME_TEST_LIMIT


def checkFindDeleted():
    global _array, _deleted

    size = len(_deleted)
    if size == 0:
        return True

    num = randint(0, size - 1)
    key = list(_deleted)[num]

    t = time.time_ns()
    user_find = user.get(key)
    dt = time.time_ns() - t

    if DEBUG and dt >= TIME_TEST_LIMIT:
        print(f"ALARM checkFindDeleted: dt >= TIME_TEST_LIMIT, dt = {dt}")

    if DEBUG and user_find is not None:
        print("ALARM checkFindDeleted: user_find is not None")

    return user_find is None and dt < TIME_TEST_LIMIT


def checkRestoreDeleted():
    global _array, _deleted

    size = len(_deleted)
    if size == 0:
        return True

    num = randint(0, size - 1)
    key = list(_deleted)[num]

    res_add = add(key, "new" + str(key))

    val = _array[key]
    t = time.time_ns()
    user_val = user.get(key)
    dt = time.time_ns() - t

    if DEBUG and dt >= TIME_TEST_LIMIT:
        print(f"ALARM checkRestoreDeleted : dt >= TIME_TEST_LIMIT, dt = {dt}")

    if DEBUG and not res_add or user_val != val:
        print("ALARM checkRestoreDeleted: not res_add or user_val != val")

    return res_add and user_val == val and dt < TIME_TEST_LIMIT


def main():
    global _array, _deleted

    _array = {}
    _deleted = set()

    user.init()

    # generate_pairs("input.txt", 100000)
    readData("input.txt")

    test_num = 10000
    error = 0

    step_show = test_num / 100
    j = 0
    print("[", end="")

    for i in range(test_num):
        case = randint(0, 3)
        res = True
        if case == 0:
            res = delete()
        elif case == 1:
            res = checkFind()
        elif case == 2:
            res = checkFindDeleted()
        elif case <= 3:
            res = checkRestoreDeleted()

        error += 0 if res else 1

        j += 1
        if j > step_show:
            j = 0
            print(".", end="")

    print("]")

    score = 100 * (test_num - error) / test_num
    score = score if score > VERIFICATION_THRESHOLD else 0
    print("Score: %d%%" % score)


if __name__ == "__main__":
    main()
