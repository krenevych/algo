#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

INF = sys.maxsize  # Умовна нескінченність

class PQElement:
    """ Клас Елемент пріорітетної черги """

    def __init__(self, key=None, priority=INF):
        """ Конструктор

        :param key: Ключ (ім'я) елементу
        :param priority: Пріорітет
        """
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        """ Встановлює пріоритет для поточного елементу

        :param priority: Пріорітет
        :return: None
        """
        self.mPriority = priority

    def key(self):
        """ Повертає ключ елемента

        :return: Ключ елемента
        """
        return self.mKey

    def __le__(self, other):
        """ Перевизначає оператор '<='

        :param other: інший елемент
        :return: True, якщо пріоритет поточного елементу менший або рівний за пріоритет іншого
        """
        return self.mPriority <= other.mPriority

    def __lt__(self, other):
        """ Перевизначає оператор '<'

        :param other: інший елемент
        :return: True, якщо пріоритет поточного елементу менший за пріоритет іншого
        """
        return self.mPriority < other.mPriority

    def __gt__(self, other):
        """ Перевизначає оператор '>'

        :param other: інший елемент
        :return: True, якщо пріоритет поточного елементу більший за пріоритет іншого
        """
        return self.mPriority > other.mPriority

    def __ge__(self, other):
        """ Перевизначає оператор '>='

        :param other: інший елемент
        :return: True, якщо пріоритет поточного елементу більший або рівний за пріоритет іншого
        """
        return self.mPriority >= other.mPriority

    def __str__(self):
        """ Перевизначає оператор "str()" для черги

        :return: None
        """
        return "(item: {}, priority: {})".format(self.mKey, self.mPriority)
