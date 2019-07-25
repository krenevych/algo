from random import randint

import user

_book_catalog = {}
_author_lst = []


def readData(fname):
    global _book_catalog, _author_lst
    dictionary = {}
    eng_lst = []
    with open(fname, encoding='utf-8') as f_in:
        for line in f_in:
            words = line.strip().split('=')
            if len(words) != 2:
                continue

            eng, translation = words[0], words[1]
            dictionary[eng] = translation
            eng_lst.append(eng)

    eng_lst.sort()
    for eng in eng_lst:
        user.addTranslation(eng, dictionary[eng])


invalid_eng = []


def read_invalid_data(fname):
    global invalid_eng
    invalid_eng = []
    with open(fname, encoding='utf-8') as f_in:
        for line in f_in:
            word = line.strip()
            invalid_eng.append(word)


def check():
    global _book_catalog, _author_lst

    size = len(eng_lst)
    errors = 0
    for i in range(100):
        num = randint(0, size - 1)
        eng = eng_lst[num]
        user_search = user.find(eng)
        if user_search != dictionary[eng]:
            errors += 1

    score = (100 - errors)
    print("Score 1: %d%%" % score)


def checkInvalid():
    global _book_catalog, _author_lst, invalid_eng

    size = len(invalid_eng)
    errors = 0
    for i in range(100):
        num = randint(0, size - 1)
        eng = invalid_eng[num]
        if eng in dictionary:
            continue

        user_search = user.find(eng)
        if user_search != "":
            errors += 1

    score = (100 - errors)
    print("Score 2: %d%%" % score)


if __name__ == "__main__":
    readData("dict_short.txt")
    read_invalid_data("invalid_words.txt")
    check()
    checkInvalid()


