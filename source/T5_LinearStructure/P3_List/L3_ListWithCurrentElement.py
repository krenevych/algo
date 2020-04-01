#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source.T5_LinearStructure.P3_List.L1_Node import Node
from source.T5_LinearStructure.P3_List.L4_ListIterator import ListIterator


class ListWithCurrent:

    def __init__(self):
        """ Конструктор - створює новий порожній список.
        """
        self.mHead = None  # Перший вузол списку
        self.mCurr = None  # Поточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список не містить жодного елемента
        """
        return self.mHead is None

    def reset(self):
        """ Зробити поточний елемент першим."""
        self.mCurr = self.mHead

    def next(self):
        """ Перейти до наступного елемента.

        Породжує виключення StopIteration, якщо наступний елемент порожній
        :return: None
        """
        if self.empty() or self.mCurr.mNext is None:
            raise StopIteration
        else:
            self.mCurr = self.mCurr.mNext

    def current(self):
        """ Отримати поточний елемент

        :return: Навантаження поточного елементу
        """
        if self.empty():
            return None
        else:
            return self.mCurr.mItem

    def insert(self, item):
        """ Вставити новий елемент у список після поточного

        :param item: елемент, що вставляється у спиоск
        :return: None
        """
        node = Node(item)
        if self.empty():
            self.mHead = node
            self.mCurr = node
        else:
            node.mNext = self.mCurr.mNext
            self.mCurr.mNext = node

    def __str__(self):
        return str(self.current())

    def __iter__(self):
        """ Спеціальний метод, що повертає ітератор для колекції
        :return: Ітератор колекції
        """
        return ListIterator(self)



l = ListWithCurrent()
l.insert(11)
l.insert(12)
l.insert(13)
l.insert(14)
l.insert(15)
l.insert(16)

# l.reset()
# l.next()
# print(l)

# it = iter(l)
# while True:
#     try:
#         print(next(l))
#     except StopIteration:
#         break


# l.reset()
# print(l)
# l.next()
# l.next()
# l.next()
# print(l)
# l.next()
#
#
# l.insert(555)
# #

# for el in l:
#     print(el)

l.reset()
print(l)
l.next()
print(l)
l.next()
print(l)
l.next()
print(l)
l.next()
print(l)
l.next()


#
# print(l)
# l.next()

l.reset()
l.insert(3333)

l.insert(3333234)

print()

for el in l:
    print(el)

