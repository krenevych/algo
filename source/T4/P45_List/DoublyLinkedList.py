class Node:
    """ Допоміжний клас - вузол двобічно зв'язаного списку """

    def __init__(self, item):
        """ Конструктор вузла

        :param item: Елемент списку
        """
        self.item = item  # дані, що пов'язані з вузлом деку
        self.next = None  # наступний вузол
        self.prev = None  # попередній вузол


class DoublyLinkedList:
    """ Двобічно зв'язаний список. """
    curr = ...  # type: Node
    first = ...  # type: Node
    last = ...  # type: Node

    def __init__(self):
        """ Конструктор списку - створює порожній список.
        """
        self.first = None  # Перший вузол списку
        self.last = None   # Останній вузол списку
        self.curr = None   # ПОточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список порожній
        """
        return self.first is None

    def set_first(self):
        """ Зробити поточними перший елемент списку """
        self.curr = self.first

    def set_last(self):
        """ Зробити поточними останній елемент списку """
        self.curr = self.last

    def next(self):
        """ Перейти до наступного елемента """
        if self.curr != self.last:
            self.curr = self.curr.next

    def prev(self):
        """	Перейти до попереднього елемента """
        if self.curr != self.first:
            self.curr = self.curr.prev

    def current(self):
        """ Отримати поточний елемент

        :return: Навантаження поточного вузла
        """
        if self.curr is not None:
            return self.curr.item
        else:
            return None

    def insert_before(self, item):
        """ Вставити новий елемент перед поточним

        поточний елемент залишається на місці
        :param item: елемент для вставки у список
        :return: None
        """
        node = Node(item)  # створюємо вузол, для нового елементу списку
        node.next = self.curr
        if self.empty():                 # вставка у порожній список
            self.first = self.last = self.curr = node
        else:
            if self.curr == self.first:  # вставка перед першим елементом
                self.first = node
            else:                        # вставка всередині списку
                node.prev = self.curr.prev
                self.curr.prev.next = node

        self.curr.prev = node

    def insert_after(self, item):
        """ Вставити новий елемент після поточного

        елемент, що був вставлений стає поточним
        :param item: елемент для вставки у список
        :return: None
        """
        node = Node(item)  # створюємо вузол, для нового елементу списку
        node.prev = self.curr
        if self.empty():  # вставка у порожній список
            self.first = self.last = self.curr = node
        else:
            if self.curr == self.last:  # вставка перед першим елементом
                self.last = node
            else:                       # вставка всередині списку
                node.next = self.curr.next
                self.curr.next.prev = node

        self.curr.next = node
        self.curr = node  # елемент, що був вставлений стає поточним

    def remove(self):
        """ Видалити поточний елемент зі списку """

        if self.empty():
            raise Exception("DoublyLinkedList: 'remove' applied to empty list")

        node = self.curr  # Запам'ятовуємо поточний вузол

        if node == self.first:  # якщо поточний вузол перший у списку
            self.first = node.next
        else:
            node.prev.next = node.next

        if node == self.last:  # якщо поточний вузол останній у списку
            self.curr = self.last = node.prev
        else:
            node.next.prev = node.prev
            self.curr = node.next

        del node  # видалення вузла

    def __str__(self):
        return str(self.current())


if __name__ == "__main__":  # For testing
    q = DoublyLinkedList()
    q.insert_after(1)
    q.insert_after(2)
    q.insert_after(3)
    q.insert_after(777)

    # q.set_first()
    q.remove()

    q.remove()

    q.remove()

    q.remove()

    q.remove()

    print(" --------------------- ")
    print(q)
    q.set_first()
    print(q)


