#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source.T7_Graphs.P3_Maizes.L1_CreateMaze import createMaze


def showMaze(maze):
    """ Функція форматованого виведення матриці лабіринту

    :param maze: матриця лабіринту
    :return:
    """
    for row in maze:
        for el in row:
            print("%3s" % (el,), end="")
        print()


if __name__ == "__main__":
    maze = createMaze(7, 7)
    showMaze(maze)
