class Node:
    """ Допоміжний клас - вузол списку. """

    def __init__(self, item):
        """ Конструктор """
        self.mItem = item   # навантаження вузла
        self.mNext = None   # посилання на наступний вузол списку


class ListWithCurrent:

    def __init__(self):
        """ Конструктор - створює новий порожній список.
        """
        self.mHead = None  # Перший вузол списку
        self.mPrev = None  # Вузол, що передує поточному елементу списку
        self.mCurr = None  # Поточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список не містить жодного елемента
        """
        return self.mHead is None

    def reset(self):
        """ Зробити поточний елемент першим.
        """
        self.mCurr = self.mHead
        self.mPrev = None

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
        node = Node(item)
        node.mNext = self.mCurr

        if self.mCurr == self.mHead:
            self.mHead = node

        if self.mPrev is not None:
            self.mPrev.mNext = node

        self.mPrev = node

    def remove(self):
        """ Видалити поточний елемент у списку

        Видалення переставляє вказівник на поточний елемент на наступний
        """
        pass  # TODO: Implement by yourself

    def __str__(self):
        return str(self.current())

    def __iter__(self):
        self.mIterator = self.mHead
        return self

    def __next__(self):
        if self.mIterator is not None:
            cur = self.mIterator.mItem
            self.mIterator = self.mIterator.mNext
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
