from source.T5_LinearStructure.P3_List.L1_Node import Node


class LinkedList:

    def __init__(self):
        """ Конструктор - створює порожній зв'язний список """
        self.mFirst = None

    def empty(self):
        """ Перевіряє чи список є порожнім

        :return: True, якщо список порожній
        """
        return self.mFirst is None

    def insert(self, item):
        """ Вставляє заданий елемент у початок списку

        :param item: елемент для вставки
        """
        node = Node(item)         # створюємо новий елемент списку
        node.mNext = self.mFirst  # наступний елемент для нового - це елемент, який є першим
        self.mFirst = node        # новий елемент стає першим у списку

    def head(self):
        """ Повертає навантаження голови списку

        :return: навантаження голови списку або None, якщо список порожній
        """
        if self.empty():
            return None
        else:
            return self.mFirst.mItem

    def tail(self):
        """ Повератє хвіст списку

        :return: хвіст списку
        """

        if self.empty():
            raise Exception("LinkedList: 'tail' applied to empty container")

        self.mFirst = self.mFirst.mNext
        return self

    def __str__(self):
        return str(self.head())


l = LinkedList()

l.insert(10)
l.insert(11)
l.insert(12)
l.insert(13)

print(l)
print(l.tail().tail())
