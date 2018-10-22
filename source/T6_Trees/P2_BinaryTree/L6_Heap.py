class Heap:
    """ Клас структура даних Купа """

    def __init__(self):
        """ Конструктор """
        self.mItems = [0]
        self.mSize = 0

    def empty(self):
        """ Перевіряє чи купа порожня

        :return: True, якщо купа порожня
        """
        return len(self.mItems) == 1

    def swap(self, i, j):
        """ Перестановка елементів у купі
        що знаходяться на заданих позиціях i та j

        :param i: перший індекс
        :param j: другий індекс
        :return: None
        """
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def siftUp(self):
        """ Дпопоміжний метод просіювання вгору

        :return: None
        """
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            i = parent

    def insert(self, *k):
        """ Вставка елемента в купу

        :param k: k[0] - Елемент, що вставляється у купу
        :return: None
        """
        self.mSize += 1
        self.mItems.append(k[0])  # Вставляємо на останню позицію,
        self.siftUp()            # просіюємо елемент вгору

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

    def siftDown(self):
        """ Просіювання вниз

        :return: None
        """
        i = 1
        while (2 * i) <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            min_child = self.minChild(left, right)
            if self.mItems[i] > self.mItems[min_child]:
                self.swap(min_child, i)
            i = min_child

    def extractMinimum(self):
        """ Повертає мінімальний елемент кучі

        :return: Мінімальний елемент кучі
        """
        root = self.mItems[1] # Запам'ятовуємо значення кореня дерева
        self.mItems[1] = self.mItems[-1]  # Переставляємо на першу позицію останній елемент (за номером) у купі
        self.mItems.pop()  # Видаляємо останній (за позицією у масиві) елемент купи
        self.mSize -= 1

        self.siftDown()  # Здійснюємо операцію просіювання вниз, для того,
                          # щоб опустити переставлений елемент на відповідну позицію у купі

        return root       # повертаємо значення кореня, яке було запам'ятовано на початку


if __name__ == "__main__":
    h = Heap()

    h.insert(17)
    h.insert(14)
    h.insert(33)
    h.insert(21)
    h.insert(27)
    h.insert(11)
    h.insert(19)
    h.insert(18)
    h.insert(9)
    h.insert(5)
    h.insert(3)
    h.insert(-10)


    while not h.empty():
        print(h.extractMinimum())

    print()
