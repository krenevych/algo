#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListIterator:
    """ Клас Ітератор """
    def __init__(self, lst):
        """ Конструктор ітератора
        :param lst: список
        """
        self.mCursor = lst.mHead  # поточна позиція ітератора у колекції

    def __next__(self):
        if self.mCursor == None:
            raise StopIteration
        else:
            curr = self.mCursor.mItem
            self.mCursor = self.mCursor.mNext
            return curr
