class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        """ Конструктор графа

        :param oriented:      Чи орієнтований граф
        :param vertex_number: Кількість вершин у графі
        """
        self.mIsOriented = oriented         # Поле чи орієнтований граф
        self.mVertexNumber = vertex_number  # Лічильник вершин у графі

        # Створюємо матрицю суміжності заповнену нулями
        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, source, destination, weight=1):
        """ Додавання ребра з кінцями в точках source та destination з вагою weight

        :param source:      Перша вернина
        :param destination: Друга вершина
        :param weight:      Вага ребра
        :return: None
        """
        assert 0 <= source < self.mVertexNumber and 0 <= destination < self.mVertexNumber
        self.mAdjacentMatrix[source][destination] = weight

        # Якщо граф є неорієнтованим, то треба встановити зворотній
        # зв'язок з вершини toVert до fromVert
        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][source] = weight

    def __str__(self):
        """ Зображення графа разом з усіма вершинами і ребрами у вигляді рядка """
        s = ''
        for vertex in self.mAdjacentMatrix:
            s = s + str(vertex) + '\n'
        return s


if __name__ == "__main__":  # Для тестування

    g = Graph(True, 7)  # Створюємо орієнтований зважений граф.

    g.addEdge(1, 2, 2)   # ребро (1, 2) з вагою 2
    g.addEdge(1, 3, 7)   # ребро (1, 3) з вагою 7
    g.addEdge(1, 4, 12)  # ребро (1, 4) з вагою 12
    g.addEdge(2, 3, 5)   # ребро (2, 3) з вагою 5
    g.addEdge(2, 5, 7)   # ребро (2, 5) з вагою 7
    g.addEdge(3, 5, 1)   # ребро (3, 5) з вагою 1
    g.addEdge(3, 6, 1)   # ребро (3, 6) з вагою 1
    g.addEdge(4, 3, 3)   # ребро (4, 3) з вагою 3
    g.addEdge(4, 6, 4)   # ребро (4, 6) з вагою 4
    g.addEdge(5, 4, 7)   # ребро (5, 4) з вагою 7
    g.addEdge(5, 6, 1)   # ребро (5, 6) з вагою 1

    print(g)
