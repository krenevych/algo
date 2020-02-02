class Deque:
    def __init__(self):
        """ Конструктор деку
        Створює порожній дек.
        """
        self.mItems = []   # Список елементів деку

    def empty(self):
        """ Перевіряє чи дек порожній

        :return: True, якщо дек порожній
        """
        return len(self.mItems) == 0

    def append(self, item):
        """ Додає елемент у кінець деку

        :param item: елемент, що додається
        :return: None
        """
        self.mItems.append(item)

    def pop(self):
        """ Повертає елемент з кінця деку.

        :return: Останній елемент у деку
        """
        if self.empty():
            raise Exception("Deque: 'popBack' applied to empty container")
        return self.mItems.pop()

    def appendleft(self, item):
        """ Додає елемент до початку деку

        :param item: елемент, що додається
        :return: None
        """
        self.mItems.insert(0, item)

    def popleft(self):
        """ Повертає елемент з початку деку.

        :return: Перший елемент у деку
        """
        if self.empty():
            raise Exception("Deque: 'popFront' applied to empty container")
        return self.mItems.pop(0)

    def __len__(self):
        """ Розмір деку

        :return: Кількість елементів у деку
        """
        return len(self.mItems)


if __name__ == "__main__":  # For testing
    D = Deque()       # Створюємо новий дек
    D.append(32)      # Додаємо елемент 32 у кінець деку
    D.append(17)      # Додаємо елемент 17 у кінець деку
    D.appendleft(99)  # Додаємо елемент 99 у початок деку
    D.appendleft(57)  # Додаємо елемент 57 у початок деку

    print(D.pop())      # Виштовхуємо останній елемент (17) з деку
    print(D.popleft())  # Виштовхуємо перший елемент (57) з деку



