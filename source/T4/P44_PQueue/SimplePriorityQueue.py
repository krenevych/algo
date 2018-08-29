

class PriorityQueue:
    def __init__(self):
        """ Конструктор """
        self.items = []   # Список елементів черги,
                          # містить пари (пріоритет, значення)

    def empty(self):
        """ Перевіряє чи чергра порожня

        :return: True, якщо черга порожня
        """
        return len(self.items) == 0

    def insert(self, priority, item):
        """ Додає елемент у чергу разом з його пріоритетом

        :param priority: пріоритет
        :param item: елемент
        :return: None
        """
        self.items.append((priority, item))

    def extract_minimum(self):
        """ Повертає елемент з черги, що має найвищий пріоритет

        :return: елемент з черги з найвищим пріоритетом
        """
        if self.empty():
            raise Exception("PriorityQueue: 'extract_minimum' applied to empty container")

        # шукаємо елемент з найвищим пріоритетом
        # у нашому випадку, той елемент для якого значення priority найменша
        minpos = 0
        for i in range(1, len(self.items)):
            if self.items[minpos][0] > self.items[i][0]:
                minpos = i

        return self.items.pop(minpos)[1]


pq = PriorityQueue()

pq.insert(3, 10)
pq.insert(2, 11)
pq.insert(7, 7)

print(pq.extract_minimum())
print(pq.extract_minimum())
print(pq.extract_minimum())
print(pq.extract_minimum())
