from source.T5_LinearStructure.P3_List.L5_Node import Node


class DoublyLinkedList:
    """ Двобічно зв'язаний список. """

    def __init__(self):
        """ Конструктор списку - створює порожній список.
        """
        self.mFirst = None  # Перший вузол списку
        self.mLast = None   # Останній вузол списку
        self.mCurr = None   # ПОточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список порожній
        """
        return self.mFirst is None

    def setFirst(self):
        """ Зробити поточними перший елемент списку """
        self.mCurr = self.mFirst

    def setLast(self):
        """ Зробити поточними останній елемент списку """
        self.mCurr = self.mLast

    def next(self):
        """ Перейти до наступного елемента """
        if self.mCurr != self.mLast:
            self.mCurr = self.mCurr.mNext

    def prev(self):
        """	Перейти до попереднього елемента """
        if self.mCurr != self.mFirst:
            self.mCurr = self.mCurr.mPrev

    def current(self):
        """ Отримати поточний елемент

        :return: Навантаження поточного вузла
        """
        if self.mCurr is not None:
            return self.mCurr.mItem
        else:
            return None

    def insertBefore(self, item):
        """ Вставити новий елемент перед поточним

        поточний елемент залишається на місці
        :param item: елемент для вставки у список
        :return: None
        """
        node = Node(item)  # створюємо вузол, для нового елементу списку
        node.mNext = self.mCurr
        if self.empty():                 # вставка у порожній список
            self.mFirst = self.mLast = self.mCurr = node
        else:
            if self.mCurr == self.mFirst:  # вставка перед першим елементом
                self.mFirst = node
            else:                        # вставка всередині списку
                node.mPrev = self.mCurr.mPrev
                self.mCurr.mPrev.next = node

        self.mCurr.mPrev = node

    def insertAfter(self, item):
        """ Вставити новий елемент після поточного

        елемент, що був вставлений стає поточним
        :param item: елемент для вставки у список
        :return: None
        """
        node = Node(item)  # створюємо вузол, для нового елементу списку
        node.mPrev = self.mCurr
        if self.empty():  # вставка у порожній список
            self.mFirst = self.mLast = self.mCurr = node
        else:
            if self.mCurr == self.mLast:  # вставка перед першим елементом
                self.mLast = node
            else:                       # вставка всередині списку
                node.mNext = self.mCurr.mNext
                self.mCurr.mNext.prev = node

        self.mCurr.mNext = node
        self.mCurr = node  # елемент, що був вставлений стає поточним

    def remove(self):
        """ Видалити поточний елемент зі списку """

        if self.empty():
            raise Exception("DoublyLinkedList: 'remove' applied to empty list")

        node = self.mCurr  # Запам'ятовуємо поточний вузол

        if node == self.mFirst:  # якщо поточний вузол перший у списку
            self.mFirst = node.mNext
        else:
            node.mPrev.mNext = node.mNext

        if node == self.mLast:  # якщо поточний вузол останній у списку
            self.mCurr = self.mLast = node.mPrev
        else:
            node.mNext.mPrev = node.mPrev
            self.mCurr = node.mNext

        del node  # видалення вузла

    def __str__(self):
        return str(self.current())


if __name__ == "__main__":  # For testing
    q = DoublyLinkedList()
    q.insertAfter(1)
    q.insertAfter(2)
    q.insertAfter(3)
    q.insertAfter(777)

    # q.set_first()
    q.remove()

    q.remove()

    q.remove()

    # q.remove()

    # q.remove()

    print(" --------------------- ")
    print(q)
    q.setFirst()
    print(q)


