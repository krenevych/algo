class Node:
    """ Допоміжний клас - вузол двобічно зв'язаного списку """

    def __init__(self, item):
        """ Конструктор вузла

        :param item: Елемент списку
        """
        self.mItem = item  # дані, що пов'язані з вузлом деку
        self.mNext = None  # наступний вузол
        self.mPrev = None  # попередній вузол