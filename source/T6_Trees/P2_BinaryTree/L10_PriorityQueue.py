from source.T6_Trees.P2_BinaryTree.L10_PQElement import PQElement


class PriorityQueue:
    """ Клас пріоритетна черга на базі структури даних Купа """

    def __init__(self):
        """ Конструктор """

        self.mItems = [PQElement(0, 0)]
        self.mSize = 0
        self.mElementsMap = {}  # Карта індексів (у масиві, що моделює чергу) елеменітів черги.
                                # Є словник з елементів (елемент, індекс)
                                # Використовується для визначення чи міститься елемент у черзі
                                # а також для швидкої зміни пріорітеру елемента у черзі

    def empty(self):
        """ Перевіряє чи купа порожня

        :return: True, якщо купа порожня
        """
        return len(self.mItems) == 1

    def insert(self, key, priority):
        """ вставки пари: (елемент, пріоритет)
        :param key:      елемент
        :param priority: пріоритет
        :return:
        """
        el = PQElement(key, priority)

        self.mSize += 1
        self.mItems.append(el)                  # Вставляємо на останню позицію,
        self.mElementsMap[key] = self.mSize    # S

        self.siftUp()          # просіюємо елемент вгору

    def extractMinimum(self):
        """ Повертає елемент черги з мінімальним пріоритетом
            Перевизначає метод батькывського класу Heap для випадку пари - (елемент, пріоритет)

        :return: Елемент черги з найвищим пріоритетом
        """

        root = self.mItems[1].item()        # Запам'ятовуємо значення кореня дерева
        self.mItems[1] = self.mItems[-1]    # Переставляємо на першу позицію останній елемент (за номером) у купі

        pos_last = self.mItems[-1].item()   # Поточна позиція останнього елемента у масиві
        self.mElementsMap[pos_last] = 1     # Переставляємо на першу позицію

        self.mItems.pop()                   # Видаляємо останній (за позицією у масиві) елемент купи
        if root in self:                    # Якщо елемент міститься у черзі
            del self.mElementsMap[root]     # Видаляємо елемент з мапи елементів

        self.mSize -= 1

        self.siftDown()   # Здійснюємо операцію просіювання вниз, для того,
                          # щоб опустити переставлений елемент на відповідну позицію у купі

        return root

    def siftDown(self):
        """ Просіювання вниз """
        i = 1
        while (2 * i) <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            min_child = self.minChild(left, right)
            if self.mItems[i] > self.mItems[min_child]:
                self.swap(min_child, i)
            i = min_child

    def siftUp(self):
        """ Дпопоміжний метод просіювання вгору """
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            i = parent

    def swap(self, i, j):
        """ Перевизначення методу батьківського класу обміну місцями елементів
            на позиціях i та j у черзі із простеженням позиції елемента у черзі.

        :param i: перший індекс
        :param j: другий індекс
        :return: None
        """
        pos_i = self.mItems[i].item()  # Поточна позиція елемента i у масиві
        pos_j = self.mItems[j].item()  # Поточна позиція елемента j у масиві
        self.mElementsMap[pos_i] = j
        self.mElementsMap[pos_j] = i

        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def minChild(self, left_child, right_child):
        """ Допоміжна функція знаходження меншого (за значенням) вузла серед нащадків поточного

        :param left_child: лівий син
        :param right_child: правий син
        :return: менший з двох синів
        """
        if right_child > self.mSize:
            return left_child
        else:
            if self.mItems[left_child] < self.mItems[right_child]:
                return left_child
            else:
                return right_child

    def __contains__(self, item):
        """ Перевизначає оператор 'in'

        :param item: Ключ
        :return: True, якщо ключ міститься у черзі
        """
        return item in self.mElementsMap

    def updatePriority(self, key, priority):
        """ Метод перерахунку пріоритету елемента.

        Працює лише у випадку підвищення пріоритету у черзі, тобто якщо
        значення параметру priority є меншим ніж поточне значення пріоритету
        Працює по принципу, замінюємо пріоритет елемента у черзі та здійснюємо просіювання вгору.
        
        :param key: Ключ
        :param priority: Новий пріоритет
        :return: True
        """

        i = self.mElementsMap[key]
        self.mItems[i].setPriority(priority)

        # просіювання вгору для елемента зі зміненим пріоритетом
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            i = parent

        return True

    def __str__(self):
        """ Перевизначає оператор "str()"

         :return: Зображення черги у вигляді рядка
         """
        res = ""
        for i in range(1, self.mSize + 1):
            res += str(self.mItems[i]) + "\n"
        return res


if __name__ == "__main__":
    h = PriorityQueue()

    h.insert(17, 11)
    h.insert(14, 10)
    h.insert(33, 9)
    h.insert(21, 8)
    h.insert(27, 7)
    h.insert(11, 6)
    h.insert(19, 5)
    h.insert(18, 4)
    h.insert(9, 3)
    h.insert(5, 2)
    h.insert(3, 9)

    print(h)

    # h.decreasePriority(11, 1)

    # print()
    #
    # print(h.extractMinimum())

    # print("==========")

    h.updatePriority(11, 5)
    # print(h)

    while not h.empty():
        print(h.extractMinimum())