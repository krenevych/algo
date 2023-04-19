#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних зв'язний (однозв'язний) список з поточним елементом.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ClassicList:
    def __init__(self):
        """ Викликається один раз на початку виконання програми. """
        self.first = None
        self.curr = None


    def empty(self):
        """ Перевіряє чи список порожній.

        :return: True, якщо список не містить жодного елемента
        """
        return self.first is None

    def reset(self):
        """ Робить перший елемент списку, поточним.

        Переставляє поточний елемент на перший елемент списку
        Гарантується, що функція не буде викликана, якщо список порожній.
        """
        self.curr = self.first

    def next(self):
        """ Перейти до наступного елемента.

        Робить поточним елементом списку, елемент що йде за поточним.
        Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
        """
        if self.curr is None or self.curr.next is None:
            raise StopIteration


        self.curr = self.curr.next

    def current(self):
        """ Повертає навантаження поточного елементу.

        Гарантується, що функція не буде викликана, якщо список порожній.
        :return: Навантаження поточного елементу
        """
        return self.curr.data

    def insert_after(self, item):
        """ Вставляє новий елемент у список після поточного.

        :param item: елемент, що вставляється у список
        """
        newNode = Node(item)
        if self.empty():  # випадок якщо список порожній
            self.curr = self.first = newNode
        else:  # випадок список НЕ порожній
            newNode.next = self.curr.next
            self.curr.next = newNode
###################################################################


myList = ClassicList()


def init():
    """ Викликається один раз на початку виконання програми. """
    global myList
    myList = ClassicList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return myList.empty()


def reset():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    myList.reset()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    myList.next()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return myList.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    myList.insert_after(item)


if __name__ == '__main__':
    myList = ClassicList()

    myList.insert_after(10)
    myList.insert_after(20)
    myList.insert_after(30)
    myList.reset()
    print(myList.current())
    myList.next()
    print(myList.current())


