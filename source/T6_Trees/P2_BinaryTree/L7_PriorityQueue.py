from source.T5_LinearStructure.P2_Queue.PriorityQueue import PQElement
from source.T6_Trees.P2_BinaryTree.L6_Heap import Heap


class PriorityQueue(Heap):
    """ Клас пріоритетна черга на базі структури даних Купа """

    def __init__(self):
        """ Конструктор """
        super().__init__()
        self.mElementsMap = {}  # Карта індексів (у масиві, що моделює чергу) елеменітів черги.
                                # Є словник з елементів (елемент, індекс)
                                # Використовується для визначення чи міститься елемент у черзі
                                # а також для швидкої зміни пріорітеру елемента у черзі

    def swap(self, i, j):
        """ Перевизначення методу батьківського класу обміну місцями елементів
            на позиціях i та j у черзі із простеженням позиції елемента у черзі.

        :param i: перший індекс
        :param j: другий індекс
        :return: None
        """
        posi = self.elems[i].item()  # Поточна позиція елемента i у масиві
        posj = self.elems[j].item()  # Поточна позиція елемента j у масиві
        self.mElementsMap[posi] = j
        self.mElementsMap[posj] = i

        super().swap(i, j)

    def __contains__(self, item):
        """ Перевизначає оператор 'in'

        :param item: Ключ
        :return: True, якщо ключ міститься у черзі
        """
        return item in self.mElementsMap

    def insert(self, *k):
        """ Перевизначення методу батьківського класу Heap для випадку вставки пари: k = (елемент, пріоритет)

        :param k: Кортеж (елемент, пріоритет)
        :return: None
        """

        assert len(k) == 2

        el = PQElement(k[0], k[1])

        self.size += 1
        self.elems.append(el)                  # Вставляємо на останню позицію,
        self.mElementsMap[k[0]] = self.size    # S

        self.sift_up()          # просіюємо елемент вгору

    def decrease_priority(self, item, priority):
        """ Метод перерахунку пріоритету елемента.

        Працює лише у випадку підвищення пріоритету у черзі, тобто якщо
        значення параметру priority є меншим ніж поточне значення пріоритету
        Працює по принципу, замінюємо пріоритет елемента у черзі та здійснюємо просіювання вгору.
        
        :param item: Ключ
        :param priority: Новий пріоритет
        :return: True
        """

        i = self.mElementsMap[item]
        self.elems[i].set_priority(priority)

        # просіювання вгору для елемента зі зміненим пріоритетом
        while i > 1:
            parent = i // 2
            if self.elems[i] < self.elems[parent]:
                self.swap(parent, i)
            i = parent

        return True

    def extract_minimum(self):
        """ Повертає елемент черги з мінімальним пріоритетом
            Перевизначає метод батькывського класу Heap для випадку пари - (елемент, пріоритет)

        :return: Елемент черги з мінімальним пріоритетом
        """

        min_el = self.elems[1][0]          # Запам'ятовуємо значення кореня дерева

        self.elems[1] = self.elems[-1]     # Переставляємо на першу позицію останній елемент (за номером) у купі

        pos_last = self.elems[-1].item()   # Поточна позиція останнього елемента у масиві
        self.mElementsMap[pos_last] = 1    # Переставляємо на першу позицію

        self.elems.pop()                   # Видаляємо останній (за позицією у масиві) елемент купи
        if min_el in self:                 # Якщо елемент міститься у черзі
            del self.mElementsMap[min_el]  # Видаляємо елемент з мапи елементів

        self.size -= 1

        self.sift_down()  # Здійснюємо операцію просіювання вниз, для того,
                          # щоб опустити переставлений елемент на відповідну позицію у купі

        return min_el

    def __str__(self):
        """ Перевизначає оператор "str()"

         :return: Зображення черги у вигляді рядка
         """
        res = ""
        for i in range(1, self.size + 1):
            res += str(self.elems[i]) + "\n"
        return res


if __name__ == "__main__":
    h = PriorityQueue()

    # h.insert(17, 11)
    # h.insert(14, 10)
    # h.insert(33, 9)
    # h.insert(21, 8)
    # h.insert(27, 7)
    h.insert(11, 6)
    h.insert(19, 5)
    h.insert(18, 4)
    h.insert(9, 3)
    h.insert(5, 2)
    h.insert(3, 9)

    print(h)

    h.decrease_priority(11, 1)

    print()
    #
    print(h.extract_minimum())

    # print("==========")

    h.decrease_priority(11, 5)
    # print(h)

    while not h.empty():
        print(h.extract_minimum())