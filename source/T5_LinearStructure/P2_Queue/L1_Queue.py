class Queue:
    """ Клас, що реалізує чергу елементів
        на базі вбудованого списку Python """

    def __init__(self):
        """ Конструктор """
        self.mItems = []  # Список елементів черги

    def empty(self):
        """ Перевіряє чи черга порожня

        :return: True, якщо черга порожня
        """
        return len(self.mItems) == 0

    def enqueue(self, item):
        """ Додає елемент у чергу (в кінець)

        :param item: елемент, що додається
        :return: None
        """
        self.mItems.append(item)

    def dequeue(self):
        """ Прибирає перший елемент з черги
            Сам елемент при цьому прибирається із черги

        :return: Перший елемент черги
        """
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")
        return self.mItems.pop(0)

    def __len__(self):
        """ Розмір черги

        :return: Кількість елементів у черзі
        """
        return len(self.mItems)


# For testing
if __name__ == "__main__":
    queue = Queue()
    queue.empty()
    queue.enqueue(32)
    queue.enqueue(17)
    queue.enqueue(99)
    queue.enqueue(26)
    queue.enqueue("New")
    len(queue)
    queue.empty()
    queue.dequeue()
