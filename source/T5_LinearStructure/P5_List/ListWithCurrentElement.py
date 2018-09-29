class Node:
    """ Допоміжний клас - вузол списку. """

    def __init__(self, item):
        """ Конструктор """
        self.item = item   # навантаження вузла
        self.next = None   # посилання на наступний вузол списку


class ListWithCurrent:

    def __init__(self):
        """ Конструктор - створює новий порожній список.
        """
        self.head = None  # Перший вузол списку
        self.prev = None  # Вузол, що передує поточному елементу списку
        self.curr = None  # Поточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список не містить жодного елемента
        """
        return self.head is None

    def reset(self):
        """ Зробити поточний елемент першим.
        """
        self.curr = self.head
        self.prev = None

    def next(self):
        """ Перейти до наступного елемента.

        Породжує виключення StopIteration, якщо наступний елемент порожній
        :return: None
        """
        if self.curr is not None:
            self.prev = self.curr
            self.curr = self.curr.next
        else:
            raise StopIteration

    def current(self):
        """ Отримати поточний елемент

        :return: Навантаження поточного елементу
        """
        if self.curr is not None:
            return self.curr.item
        else:
            return None

    def insert(self, item):
        """ Вставити новий елемент у список перед поточним

        :param item: елемент, що вставляється у спиоск
        :return: None
        """
        node = Node(item)
        node.next = self.curr

        if self.curr == self.head:
            self.head = node

        if self.prev is not None:
            self.prev.next = node

        self.prev = node

    def remove(self):
        """ Видалити поточний елемент у списку

        Видалення переставляє вказівник на поточний елемент на наступний
        """
        pass  # TODO: Implement by yourself

    def __str__(self):
        return str(self.current())

    def __iter__(self):
        self._iterator = self.head
        return self

    def __next__(self):
        if self._iterator is not None:
            cur = self._iterator.item
            self._iterator = self._iterator.next
            return cur
        else:
            raise StopIteration


l = ListWithCurrent()
l.insert(11)
l.insert(12)
l.insert(13)
l.insert(14)
l.insert(15)
l.insert(16)

l.reset()
l.next()
print(l)

it = iter(l)
while True:
    try:
        print(next(l))
    except StopIteration:
        break


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
