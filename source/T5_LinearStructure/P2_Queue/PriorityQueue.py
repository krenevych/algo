from builtins import print
from random import Random


class PQElement:
    """ Клас Елемент пріорітетної черги """

    INF = 100000                   # Умовна нескінченність

    def __init__(self, item=None, priority=INF):
        """ Конструктор

        :param item: Ключ (ім'я) елементу
        :param priority: Пріорітет
        """
        self.mItem = item
        self.mPriority = priority

    def setPriority(self, priority):
        """ Встановлює пріоритет для поточного елементу

        :param priority: Пріорітет
        :return: None
        """
        self.mPriority = priority

    def setItem(self, item):
        """ Встановлення ключа поточного елементу

        :param item: Нове значення ключа
        :return: None
        """
        self.mItem = item

    def priority(self):
        """ Повертає поточний пріорітет елементу

        :return: Поточне пріорітет елементу
        """
        return self.mPriority

    def item(self):
        """ Повертає ключ елемента

        :return: Ключ елемента
        """
        return self.mItem

    def __getitem__(self, item):
        """ Перевизначає оператор '[]' для читання

        :param item: 0 - для того, щоб взяти ключ елемента, 1 - його пріорітет
        :return: Ключ/пріоритет
        """
        if item == 0:
            return self.mItem
        elif item == 1:
            return self.mPriority
        else:
            raise IndexError

    def __setitem__(self, key, value):
        """ Перевизначає оператор '[]' для запису

        :param key: 0 - для того, щоб взяти ключ елемента, 1 - його пріорітет
        :param value: Ключ/пріоритет
        :return: None
        """
        if key == 0:
            self.mItem = value
        elif key == 1:
            self.mPriority = value
        else:
            raise IndexError

    def __str__(self):
        """ Перевизначає оператор "str()" для черги

        :return: None
        """
        return "(item: {}, priority: {})".format(self.mItem, self.mPriority)

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


class PriorityQueue:
    """ Клас пріоритетна черга на базі класичного списку Python
    """
    def __init__(self):
        """ Конструктор """
        # Список, що буде містити елементи черги разом з їхніми пріоритетами
        self.items = []

    def insert(self, item, priority):
        """ Вставляє елемент разом з його пріоритетом до черги

        :param item: Елемент
        :param priority: Пріоритет
        :return: None
        """
        pqitem = PQElement(item, priority)
        self.items.append(pqitem)

    def extractMinimum(self):
        """ Повертає елемент з чеги з найвищим пріорітетом
            У цій реалізації черги з пріоритетом, найвищий пріоритет для
            вилучення має той елемент, у якого поле priority має найменше значення

        :return: Елемент з найвищим пріоритетом
        """

        if self.empty():
            raise Exception("Queue: 'extract' applied to empty container")

        # шукаємо елемент з найвищим пріоритетом
        minpos = 0
        for i in range(1, len(self.items)):

            curMin = self.items[minpos]
            cur = self.items[i]

            if curMin[1] > cur[1]:
                minpos = i

        return self.items.pop(minpos).item()

    def decreasePriority(self, item, priority):
        """ Півищує пріоритет заданого елементу заданим значенням

        :param item: Елемент черги
        :param priority: Новий пріоритет
        :return: None
        """
        for el in self.items:
            if el.item() == item:
                el.setPriority(priority)

    def empty(self):
        """ Перевіряє чи черга порожня

        :return: True, якщо черга порожня
        """
        return len(self.items) == 0

    def size(self):
        """ Розмір черги

        :return: Кількість елементів у черзі
        """
        return len(self.items)

    def __str__(self):
        """ Перевизначає оператор "str()"
        :return: None
        """
        res = ""
        for item in self.items:
            res += str(item) + "\n"
        return res

    def __contains__(self, item):
        """ Перевизначає оператор 'in' для черги

        :param item: Елемент
        :return: True, якщо елемент міститься чергі
        """
        for el in self.items:
            if item == el.item():
                return True

        return False


def constructPQ(pq):
    for i in range(9, 0, -1):
        pq.insert(i * 10, i)

def constructPQElement(el, pr):
    return PQElement(el, pr)

def constructRandomPQ(pq, points):
    rnd = Random()
    for i in range(points):
        item = rnd.randint(100, 200)
        priority = rnd.randint(10, 30)
        pq.insert(item, priority)


if __name__ == "__main__":

    e1 = constructPQElement("XXX", 1)
    e2 = constructPQElement("ZZZ", 2)

    print(e1)
    print(e2)

    print(e1 < e2)
    print(e1 <= e2)
    print(e1 >= e2)
