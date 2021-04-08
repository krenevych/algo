#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class List:
    def __init__(self):
        self.front : Node = None
        self.cur : Node = None

    def empty(self):
        """ Перевіряє чи список порожній.

        :return: True, якщо список не містить жодного елемента
        """
        return self.front is None

    def reset(self):
        """ Робить перший елемент списку, поточним.

        Переставляє поточний елемент на перший елемент списку
        Гарантується, що функція не буде викликана, якщо список порожній.
        """
        self.cur = self.front

    def next(self):
        """ Перейти до наступного елемента.

        Робить поточним елементом списку, елемент що йде за поточним.
        Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
        """
        if self.cur is None or self.cur.next is None:
            raise StopIteration

        self.cur = self.cur.next

    def current(self):
        """ Повертає навантаження поточного елементу.

        Гарантується, що функція не буде викликана, якщо список порожній.
        :return: Навантаження поточного елементу
        """
        return self.cur.item

    def insert_after(self, item):
        """ Вставляє новий елемент у список після поточного.

        :param item: елемент, що вставляється у список
        """
        node = Node(item)
        if self.empty():
            self.cur = self.front = node
        else:
            node.next = self.cur.next
            self.cur.next = node

    def prev(self):
        if self.cur == self.front:
            return None
        else:
            p = self.front
            while True:
                if p.next == self.cur:
                    return p
                p = p.next


    def insert_before(self, item):
        """ Вставляє новий елемент у список перед поточним.

        :param item: елемент, що вставляється у список
        """
        if self.empty():
            self.insert_after(item)
            return

        node = Node(item)
        if self.cur == self.front:
            node.next = self.cur
            self.front = node
            return

        pre = self.prev()
        node.next = self.cur
        pre.next = node



    def delete(self):
        """ Видаляє поточний елемент.

        Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
        Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
        """
        if self.empty():
            pass
            return

        if self.cur == self.front:
            self.cur = self.front = self.front.next
            return

        pre = self.prev()
        pre.next = self.cur.next
        self.cur = pre.next

        if self.cur == None:
            self.cur = pre

    def damp(self):
        """ Повертає масив у якому записані всі елементи поточного списку.

        :return: список list елементів списку
        """
        self.reset()
        res = []
        while True:
            try:
                res.append(self.current())
                self.next()
            except StopIteration:
                return res

lst = List()

def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = List()

def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return lst.empty()


def reset():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.reset()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    lst.next()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return lst.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    lst.insert_after(item)


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    pass


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    """
    pass


def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return []
