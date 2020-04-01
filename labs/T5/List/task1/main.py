#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import user

input_file = "input2.txt"


def main():

    _lst = []
    error = 0
    test_num = 0

    user.init()
    _cur = -1

    with open(input_file) as f_in:
        for line in f_in:
            pair = line.strip().split()

            if len(pair) != 1 and len(pair) != 2:
                continue

            key = pair[0]
            item = 0
            if len(pair) == 2:
                item = int(pair[1])

            if key == "empty":
                test_num += 1
                out_empty = user.empty()
                lst_empty = len(_lst) == 0
                if out_empty != lst_empty:
                    error += 1

            elif key == "reset":
                if len(_lst) == 0:
                    continue

                _cur = 0
                user.reset()

            elif key == "next":
                if len(_lst) == 0:
                    continue

                if _cur < len(_lst) - 1:
                    _cur += 1
                    user.next()

            elif key == "current":
                if len(_lst) == 0:
                    continue

                test_num += 1
                out_current = user.current()
                lst_current = _lst[_cur]
                if out_current != lst_current:
                    error += 1

            elif key == "insert_after":
                _lst.insert(_cur + 1, item)
                user.insert_after(item)
                if len(_lst) == 1:
                    _cur = 0

            elif key == "insert_before":
                _lst.insert(_cur, item)
                user.insert_before(item)
                if len(_lst) == 1:
                    _cur = 0
                else:
                    _cur += 1

            elif key == "delete":
                if len(_lst) == 0:
                    continue

                user.delete()
                _lst.pop(_cur)
                if _cur == len(_lst):
                    _cur = len(_lst) - 1

            elif key == "damp":
                test_num += 1
                out = user.damp()
                if len(_lst) !=len(out):
                    error += 1
                else:
                    for i in range(len(_lst)):
                        if _lst[i] != out[i]:
                            error += 1
                            break

        score = 100 * (test_num - error) / test_num
        print("Score: %d%%" % score)


if __name__ == "__main__":
    main()
