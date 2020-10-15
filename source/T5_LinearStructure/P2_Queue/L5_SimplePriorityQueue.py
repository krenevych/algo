

class PriorityQueue:
    def __init__(self):
        """ Конструктор """
        self.mItems = []   # Список елементів черги, містить пари (ключ, пріоритет)

    def empty(self):
        """ Перевіряє чи чергра порожня

        :return: True, якщо черга порожня
        """
        return len(self.mItems) == 0

    def insert(self, key, priority):
        """ Додає елемент у чергу разом з його пріоритетом

        :param key: елемент
        :param priority: пріоритет
        :return: None
        """
        self.mItems.append((key, priority))

    def extractMinimum(self):
        """ Повертає елемент з черги, що має найвищий пріоритет

        :return: елемент з черги з найвищим пріоритетом
        """
        if self.empty():
            raise Exception("PriorityQueue: 'extract_minimum' applied to empty container")

        # шукаємо елемент з найвищим пріоритетом
        # у нашому випадку, той елемент для якого значення priority найменша
        minpos = 0
        for i in range(1, len(self.mItems)):
            if self.mItems[minpos][1] > self.mItems[i][1]:
                minpos = i

        return self.mItems.pop(minpos)[0]


pq = PriorityQueue()

pq.insert(1, 13)
pq.insert(2, 6)
pq.insert(3, 1)

print(pq.extractMinimum())
print(pq.extractMinimum())
print(pq.extractMinimum())
# print(pq.extractMinimum())
