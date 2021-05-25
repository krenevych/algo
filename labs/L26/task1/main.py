import sys

INF = sys.maxsize  # Умовна нескінченність


class PQElement:
    """ Клас Елемент пріорітетної черги """

    def __init__(self, key=None, priority=INF):
        """ Конструктор

        :param key: Ключ (ім'я) елементу
        :param priority: Пріорітет
        """
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        """ Встановлює пріоритет для поточного елементу

        :param priority: Пріорітет
        :return: None
        """
        self.mPriority = priority

    def key(self):
        """ Повертає ключ елемента

        :return: Ключ елемента
        """
        return self.mKey

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

    def __str__(self):
        """ Перевизначає оператор "str()" для черги

        :return: None
        """
        return "(item: {}, priority: {})".format(self.mKey, self.mPriority)


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
        self.mItems.append(el)  # Вставляємо на останню позицію,
        self.mElementsMap[key] = self.mSize  # S

        self.siftUp()  # просіюємо елемент вгору

    def extractMinimum(self):
        """ Повертає елемент черги з найвищим пріоритетом
        у цій реалізації пріоритетної черги вважається чим меншим є значення
        поля пріоритету тим вищим є пріоритет елементу у черзі.
        :return: Елемент черги з найвищим пріоритетом
        """

        root = self.mItems[1].key()  # Запам'ятовуємо значення кореня дерева

        self.swap(1, -1)  # Переставляємо на першу позицію останній елемент (за номером) у купі

        self.mItems.pop()  # Видаляємо останній (за позицією у масиві) елемент купи
        del self.mElementsMap[root]  # Видаляємо елемент з мапи елементів

        self.mSize -= 1

        self.siftDown()  # Здійснюємо операцію просіювання вниз, для того,
        # щоб опустити переставлений елемент на відповідну позицію у купі

        return root

    def swap(self, i, j):
        """ Перевизначення методу батьківського класу обміну місцями елементів
            на позиціях i та j у черзі із простеженням позиції елемента у черзі.

        :param i: перший індекс
        :param j: другий індекс
        :return: None
        """
        pos_i = self.mItems[i].key()  # Поточна позиція елемента i у масиві
        pos_j = self.mItems[j].key()  # Поточна позиція елемента j у масиві
        self.mElementsMap[pos_i] = j
        self.mElementsMap[pos_j] = i

        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def siftDown(self):
        """ Просіювання вниз """
        i = 1
        while (2 * i) <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            min_child = self.minChild(left, right)
            if self.mItems[i] > self.mItems[min_child]:
                self.swap(min_child, i)
            else:
                break
            i = min_child

    def siftUp(self):
        """ Дпопоміжний метод просіювання вгору """
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            else:
                break
            i = parent

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
        self.mItems[i].updatePriority(priority)

        # просіювання вгору для елемента зі зміненим пріоритетом
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            else:
                break
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


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbour = {}  # список (словник ключ_вершини: вага ребра) сусідів
        self.distance = INF
        self.source = None  # використовується для побудови шляху - вершина з якої ми прийшли у поточну вершину

    def __str__(self):
        return str(self.key) + ":" + str(*self.neighbour.keys())


def main():
    graph = []
    with open("input.txt") as in_file:
        vertices, edges = map(int, in_file.readline().split())
        for i in range(vertices + 1):
            graph.append(Vertex(i))

        for e in range(edges):
            source, destination, weight = map(int, in_file.readline().split())
            graph[source].neighbour[destination] = weight
            graph[destination].neighbour[source] = weight

    weight = constractSpanningTree(graph)
    print(weight)


def constractSpanningTree(graph):

    for v in graph:
        v.distance = INF
        v.source = None

    start = 1

    graph[start].distance = 0
    pq = PriorityQueue()
    for key_ver in range(len(graph)):
        pq.insert(key_ver, graph[key_ver].distance)

    while not pq.empty():
        vert = pq.extractMinimum()

        for neigb, weight in graph[vert].neighbour.items():
            if neigb in pq and weight < graph[neigb].distance:
                graph[neigb].distance = weight
                graph[neigb].source = vert
                pq.updatePriority(neigb, graph[neigb].distance)


    spanningTree = []
    vertices = len(graph)
    for i in range(vertices + 1):
        spanningTree.append(Vertex(i))


    spanningTreeWeight = 0
    for destination in range(vertices):
        if graph[destination].source is not None:
            spanningTreeWeight += graph[destination].distance
            source = graph[destination].source
            spanningTree[destination].neighbour[source] = graph[destination].distance


    return spanningTreeWeight


if __name__ == "__main__": main()
