#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        """ Викликається один раз на початку виконання програми. """
        self.first = Node("Fake First")
        self.last = Node("Fake Last")
        self.first.next = self.last
        self.last.prev = self.first

        self.curr = self.last

    def empty(self):
        """ Перевіряє чи список порожній.

        :return: True, якщо список не містить жодного елемента
        """
        return self.curr == self.last

    def set_first(self):
        """ Робить перший елемент списку, поточним.

        Переставляє поточний елемент на перший елемент списку.
        Гарантується, що функція не буде викликана, якщо список порожній.
        """
        self.curr = self.first.next

    def set_last(self):
        """ Робить останній елемент списку, поточним

        Переставляє поточний елемент на останній елемент списку
        Гарантується, що функція не буде викликана, якщо список порожній.
        """
        self.curr = self.last.prev

    def next(self):
        """ Перейти до наступного елемента.

        Робить поточним елементом списку, елемент що йде за поточним.
        Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
        """
        if self.curr == self.last or self.curr.next == self.last:
            raise StopIteration

        self.curr = self.curr.next

    def prev(self):
        """ Перейти до попереднього елемента списка.

        робить поточним елементом елемент списку, що йде перед поточним.
        Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
        """
        if self.curr.prev == self.first:
            raise StopIteration

        self.curr = self.curr.prev

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

        if self.empty():
            self.insert_before(item)
            return

        newNode = Node(item)

        newNode.prev = self.curr
        newNode.next = self.curr.next

        self.curr.next.prev = newNode
        self.curr.next = newNode

        if self.curr == self.last:
            self.curr = newNode

    def insert_before(self, item):
        """ Вставляє новий елемент у список перед поточним.

        :param item: елемент, що вставляється у список
        """
        newNode = Node(item)
        newNode.next = self.curr
        newNode.prev = self.curr.prev

        self.curr.prev.next = newNode
        self.curr.prev = newNode

        if self.curr == self.last:
            self.curr = newNode

    def delete(self):
        """ Видаляє поточний елемент.

        Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
        Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
        Гарантується, що функція не буде викликана, якщо список порожній.
        """
        cur = self.curr
        self.curr.prev.next = cur.next
        self.curr.next.prev = cur.prev
        self.curr = cur.next

        if self.curr == self.last and self.last.prev != self.first:
            self.curr = self.last.prev

myList = DoubleLinkedList()

def init():
    """ Викликається один раз на початку виконання програми. """
    global myList
    myList = DoubleLinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return myList.empty()


def set_first():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    myList.set_first()


def set_last():
    """ Робить останній елемент списку, поточним

    Переставляє поточний елемент на останній елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    myList.set_last()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    myList.next()


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    myList.prev()


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


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    myList.insert_before(item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    myList.delete()


if __name__ == '__main__':
    myList = DoubleLinkedList()
    myList.insert_after(10)
    myList.insert_after(20)
    myList.next()
    myList.insert_after(30)
    myList.insert_before(40)
    print(myList.current())