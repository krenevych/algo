import time
from user import HashTable
from random import randint

N_MAXKEY = 10000000
TIME_MULTIPLIER = 100000
TIME_TEST_LIMIT = 200
VERIFICATION_THRESHOLD = 70

_array = {}
_deleted = set()
table = HashTable()



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
    t = time.time()
    table.set(key, value)
    dt = (time.time() - t) * TIME_MULTIPLIER
    if key in _deleted:
        _deleted.remove(key)

    return dt < TIME_TEST_LIMIT


def delete():
    global _array, _deleted
    size = len(_array)

    num = randint(0, size - 1)
    key = list(_array)[num]

    del _array[key]
    _deleted.add(key)

    t = time.time()
    table.delete(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

    return dt < TIME_TEST_LIMIT


def checkFind():
    global _array, _deleted
    size = len(_array)
    num = randint(0, size - 1)
    key = list(_array)[num]

    val = _array[key]

    t = time.time()
    user_val = table.get(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

    return user_val == val and dt < TIME_TEST_LIMIT


def checkFindDeleted():
    global _array, _deleted

    size = len(_deleted)
    if size == 0:
        return True

    num = randint(0, size - 1)
    key = list(_deleted)[num]

    t = time.time()
    user_find = table.get(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

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
    t = time.time()
    user_val = table.get(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

    return res_add and user_val == val and dt < TIME_TEST_LIMIT


def checkIteratator():
    table_key = set()
    for key in table:
        if key == None or key not in _array:
            return False
        table_key.add(key)

    for key in _array:
        if key not in table_key:
            return False

    return True



def main():
    global _array, _deleted, table

    _array = {}
    _deleted = set()

    table = HashTable()

    # generate_pairs("input.txt", 100000)
    readData("input.txt")

    test_num = 1000
    error = 0

    step_show = test_num / 100
    j = 0
    print("[", end="")

    for i in range(test_num):
        case = randint(0, 7)
        # print(case)
        res = True
        if case == 0:
            res = delete()
        elif case <= 2:
            res = checkFind()
        elif case <= 4:
            res = checkFindDeleted()
        elif case <= 6:
            res = checkRestoreDeleted()
        elif case <= 7:
            res = checkIteratator()

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
