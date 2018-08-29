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
        self.prev = None  # Вузол, що передує поточному елементу списку
        self.curr = None  # Поточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список не містить жодного елемента
        """
        return self.curr is None

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
        node = Node(item)  # Створюємо вузол для елементу
        node.next = self.curr

        if self.empty():   # список порожній
            node.next = node
            self.curr = node
        else:   # список містить принаймні один вузол
            self.prev.next = node

        self.prev = node

    def __str__(self):
        return str(self.current())


l = ListWithCurrent()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)

# print(l)
# l.next()
# print(l)
#
# l.next()
#
# print("===========")
#
# l.insert(777)

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
