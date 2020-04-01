from source.T5_LinearStructure.P3_List.L1_Node import Node


class CircularLinkedList:

    def __init__(self):
        """ Конструктор - створює новий порожній список.
        """
        self.mCurr = None  # Поточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список не містить жодного елемента
        """
        return self.mCurr is None

    def next(self):
        """ Перейти до наступного елемента.

        Породжує виключення StopIteration, якщо наступний елемент порожній
        :return: None
        """
        if self.empty():
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
        """ Вставити новий елемент у список перед поточним

        :param item: елемент, що вставляється у спиоск
        :return: None
        """

        node = Node(item)
        if self.empty():
            node.mNext = node
            self.mCurr = node
        else:
            node.mNext = self.mCurr.mNext
            self.mCurr.mNext = node


    def __str__(self):
        return str(self.current())


l = CircularLinkedList()
l.insert(0)
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)


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
print(l)
l.next()
print(l)
l.next()
print(l)
l.next()
print(l)
