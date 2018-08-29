
class Node:
    """ Допоміжний клас - вузол деку """

    def __init__(self, item):
        """ Конструктор вузла деку

        :param item: Елемент деку
        """
        self.item = item  # поле, що містить елемент деку
        self.next = None  # наступний вузол
        self.prev = None  # попередній вузол


class Deque:
    """ Реалізує дек як рекурсивну структуру. """

    def __init__(self):
        """ Конструктор деку - Створює порожній дек.
        """
        self.front = None  # Посилання на перший елемент деку
        self.back = None   # Посилання на останній елемент деку

    def empty(self):
        """ Перевіряє чи дек порожній

        :return: True, якщо дек порожній
        """
        return self.front is None and self.back is None

    def appendleft(self, item):
        """ Додає елемент до початку деку

        :param item: елемент, що додається
        :return: None
        """
        node = Node(item)           # створюємо новий вузол деку
        node.next = self.front      # наступний вузол для нового - це елемент, який є першим
        if not self.empty():        # якщо додаємо до непорожнього деку
            self.front.prev = node  # новий вузол стає попереднім для першого
        else:
            self.back = node  # якщо додаємо до порожнього деку, новий вузол буде й останнім
        self.front = node     # новий вузол стає першим у деку

    def popleft(self):
        """ Повертає елемент з початку деку.

        :return: Перший елемент у деку
        """
        if self.empty():
            raise Exception('pop_front: Дек порожній')
        node = self.front       # node - перший вузол деку
        item = node.item        # запам'ятовуємо навантаження
        self.front = node.next  # першим стає наступний вузлом деку
        if self.front is None:  # якщо в деку був 1 елемент
            self.back = None    # дек стає порожнім
        else:
            self.front.prev = None  # інакше перший елемент посилається на None
        del node                    # Видаляємо вузол
        return item

    # методи append та pop повністю симетричні appendleft та popleft відповідно
    def append(self, item):
        """ Додає елемент у кінець деку

        :param item: елемент, що додається
        :return: None
        """
        elem = Node(item)
        elem.prev = self.back
        if not self.empty():
            self.back.next = elem
        else:
            self.front = elem
        self.back = elem

    def pop(self):
        """ Повертає елемент з кінця деку.

        :return: Останній елемент у деку
        """
        if self.empty():
            raise Exception('pop_back: Дек порожній')
        node = self.back
        item = node.item
        self.back = node.prev
        if self.back is None:
            self.front = None
        else:
            self.back.next = None
        del node
        return item

    def __del__(self):
        """ Деструктор - використовується для коректного видалення
            усіх елементів деку у разі видалення самого деку

        :return: None
        """
        while self.front is not None:  # проходимо по всіх елементах деку
            node = self.front  # запам'ятовуємо посилання на елемент
            self.front = self.front.next  # переходимо до наступного елементу
            del node  # видаляємо елемент
        self.back = None


def clone(deque):
    """ Допоміжний метод дублування деку

    :param deque: Дек
    :return: Копія деку
    """
    res_deque = Deque()
    tmp_deque = Deque()
    while not deque.empty():
        front = deque.dequeue()
        tmp_deque.append(front)

    while not tmp_deque.empty():
        front = tmp_deque.popleft()
        res_deque.append(front)
        deque.enqueue(front)

    return res_deque


# For testing
if __name__ == "__main__":
    q = Deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.pop())
    print(q.pop())
    q.append(15)
    q.appendleft(155)

    print(q.popleft())
    print(q.popleft())

    q.append(777)
    print(q.pop())
    # print(q.pop_back())
    # print(q.dequeue())
    # print(q.dequeue())
