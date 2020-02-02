
class Node:
    """ Допоміжний клас - вузол черги.

    Вузлол зберігає у собі навантаження - певну інформаційну частину
    (іншу структуру або тип даних) - та посилання на наступний вузол
    """

    def __init__(self, item):
        """ Конструктор

        :param item: навантаження вузла
        """
        self.mItem = item   # поле для зберігання навантаження
        self.mNext = None   # посилання на наступний вузол черги


class Queue:
    """ Клас, що реалізує чергу елементів
        як рекурсивну структуру """

    def __init__(self):
        """ Конструктор """
        self.mFront = None  # Посилання на початок черги
        self.mBack = None   # Посилання на кінець черги

    def empty(self):
        """ Перевіряє чи черга порожня

        :return: True, якщо черга порожня
        """
        # Насправді досить перевіряти лише одне з полів front або back
        return self.mFront is None and self.mBack is None

    def enqueue(self, item):
        """ Додає елемент у чергу (в кінець)

        :param item: елемент, що додається
        :return: None
        """

        new_node = Node(item)      # Створюємо новий вузол черги
        if self.empty():           # Якщо черга порожня
            self.mFront = new_node  # новий вузол робимо початком черги
        else:
            self.mBack.mNext = new_node  # останній вузол черги посилається на новий вузол

        self.mBack = new_node       # Останній вузол вказує на новий вузол

    def dequeue(self):
        """ Прибирає перший елемент з черги
            Сам елемент при цьому прибирається із черги

        :return: Навантаження голови черги (перший елемент)
        """
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")

        current_front = self.mFront       # запам'ятовуємо поточну голову черги
        item = current_front.item        # запам'ятовуємо навантаження першого вузла черги
        self.mFront = self.mFront.next     # замінюємо перший вузол наступним
        del current_front                # видаляємо запам'ятований вузол

        if self.mFront is None:  # Якщо голова черги стала порожньою
            self.mBack = None    # Черга порожня = хвіст черги теж порожній
        return item


# For testing
if __name__ == "__main__":
    q = Queue()
    q.enqueue(13)
    q.enqueue(14)
    print(q.dequeue())
    q.enqueue(15)
    q.enqueue(15)

    print(q.dequeue())
    print(q.dequeue())


    q.enqueue(777)
    print(q.dequeue())
    print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
