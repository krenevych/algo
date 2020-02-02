from source.T5_LinearStructure.P3_List.L1_Node import Node


class CircularLinkedList:

    def __init__(self):
        """ Конструктор - створює новий порожній список.
        """
        self.mPrev = None  # Вузол, що передує поточному елементу списку
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
        if self.mCurr is not None:
            self.mPrev = self.mCurr
            self.mCurr = self.mCurr.mNext
        else:
            raise StopIteration

    def current(self):
        """ Отримати поточний елемент

        :return: Навантаження поточного елементу
        """
        if self.mCurr is not None:
            return self.mCurr.mItem
        else:
            return None

    def insert(self, item):
        """ Вставити новий елемент у список перед поточним

        :param item: елемент, що вставляється у спиоск
        :return: None
        """
        node = Node(item)  # Створюємо вузол для елементу
        node.mNext = self.mCurr

        if self.empty():   # список порожній
            node.mNext = node
            self.mCurr = node
        else:   # список містить принаймні один вузол
            self.mPrev.mNext = node

        self.mPrev = node

    def remove(self):
        """ Видалити поточний елемент у списку """
        pass  # TODO: Implement by yourself

    def __str__(self):
        return str(self.current())


l = CircularLinkedList()
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
