import time
from random import randint

import user

MSEC_MULTIPLIER = 1000
TIME_THRESHOLD_MSEC = 30

dictionary = {}
eng_lst = []


def readData(fname):
    global dictionary, eng_lst
    dictionary = {}
    eng_lst = []
    eng, translation = "", ""
    with open(fname, encoding='utf-8') as f_in:
        for line in f_in:
            word = line.strip()
            if eng == "":
                eng = word
            else:
                translation = word
                dictionary[eng] = translation
                eng_lst.append(eng)
                eng, translation = "", ""

    # eng_lst.sort()
    for eng in eng_lst:
        user.addTranslation(eng, dictionary[eng])


invalid_eng = []


def read_invalid_data(fname):
    global dictionary, invalid_eng
    invalid_eng = []
    with open(fname, encoding='utf-8') as f_in:
        for line in f_in:
            word = line.strip()
            if word in dictionary:
                continue

            invalid_eng.append(word)


def check(test_cases_num):
    global dictionary, eng_lst

    size = len(eng_lst)
    errors = 0
    for i in range(test_cases_num):
        num = randint(0, size - 1)
        eng = eng_lst[num]

        t = time.time()
        user_search = user.find(eng)
        t1 = time.time()
        dt = t1 - t
        dt *= MSEC_MULTIPLIER
        # print('eng = %s, user_search = %s,  find time: %d ms' % (eng, user_search, dt))
        # print('find time: %d ms' % dt)
        if user_search != dictionary[eng] or dt > TIME_THRESHOLD_MSEC:
            errors += 1

    return errors


def checkInvalid(test_cases_num):
    global dictionary, eng_lst, invalid_eng

    size = len(invalid_eng)
    errors = 0
    for i in range(test_cases_num):
        num = randint(0, size - 1)
        eng = invalid_eng[num]
        if eng in dictionary:
            continue

        t = time.time()
        user_search = user.find(eng)
        t1 = time.time()
        dt = t1 - t
        dt *= MSEC_MULTIPLIER
        # print('eng = %s, user_search = %s,  find time: %d ms' % (eng, user_search, dt))
        # print('find time: %d ms' % dt)
        if user_search != "" or dt > TIME_THRESHOLD_MSEC:
            errors += 1

    return errors


def generate_invalid(fname, N):
    f_out = open(fname, "w", encoding='utf-8')
    for i in range(N):
        chars = randint(3, 20)
        word = ""
        for j in range(chars):
            ch = randint(0, 25)
            word += chr(ord('a') + ch)
        print(word, file=f_out, end="\n")
    f_out.close()


def main():
    readData("dictionary.txt")
    # generate_invalid("invalid_words.txt", 1000)
    read_invalid_data("invalid_words.txt")
    valid_test_num = 100
    inval_test_num = 100
    valid_score = valid_test_num - check(valid_test_num)
    inval_score = inval_test_num - checkInvalid(inval_test_num)

    score = 100 * (valid_score + inval_score) / (valid_test_num + inval_score)
    score = score if score > 50 else 0
    print("Score: %d%%" % score)


if __name__ == "__main__":
    main()

