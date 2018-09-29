class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        """ Конструктор графа

        :param oriented: Чи орієнтований граф
        :param vertex_number: Кількість вершин у графі
        """
        self.mIsOriented = oriented         # Поле чи орієнтований граф
        self.mVertexNumber = vertex_number  # Лічильник вершин у графі

        # Створюємо матрицю суміжності заповнену нулями
        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def add_edge(self, source, destination, weight=1):
        """ Додавання ребра з кінцями в точках source та destination з вагою weight

        :param source: Перша вернина
        :param destination: Друга вершина
        :param weight: Вага ребра
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

    g = Graph(True, 6)  # Створюємо орієнтований граф

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    print(g)
