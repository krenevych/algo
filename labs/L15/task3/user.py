#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

"""
Реалізуйте структуру даних двобічнозв'язний список з поточним елементом.
"""

front : Node = None
last  : Node = None
curr  : Node = None

def init():
    """ Викликається один раз на початку виконання програми. """
    global front, last, curr
    front =  last = curr = None


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    global front, last, curr
    return curr == None


def set_first():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global front, last, curr
    curr = front

def set_last():
    """ Робить останній елемент списку, поточним

    Переставляє поточний елемент на останній елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global front, last, curr
    curr = last


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    global front, last, curr
    if curr == last:
        raise StopIteration

    curr = curr.next


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    global front, last, curr
    if curr == front:
        raise StopIteration

    curr = curr.prev


def current():
    """ Повертає навантаження поточного елементу.

    :return: Навантаження поточного елементу
    """
    global front, last, curr
    if curr == None:
        return None

    return curr.item


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    global front, last, curr
    node = Node(item)
    if empty():
        front = last = curr = node
        return

    node.next = curr.next
    node.prev = curr

    curr.next = node
    if node.next != None:
        node.next.prev = node

    curr = node

def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    global front, last, curr
    node = Node(item)
    if empty():
        front = last = curr = node
        return

    node.prev = curr.prev
    node.next = curr

    curr.prev = node
    if node.prev != None:
        node.prev.next = node


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global front, last, curr
    if front == last:
        front = last = curr = None
        return

    if curr.prev != None:
        curr.prev.next = curr.next

    if curr.next != None:
        curr.next.prev = curr.prev
        curr = curr.next
    else:
        curr = curr.prev


