from source.T7_Graphs.P1_Definitions.L1_Graph import Graph


class GraphWithData(Graph):
    """ Клас нащадок класу Graph
        Містить поле навантаження вершини та методи роботи з ним
    """

    DEFAULT_VERTEX_DATA = 0  # типове навантаження на вершину

    def __init__(self, oriented: bool = False, vertices: int = 20):
        """ Конструктор
        :param oriented: Чи орієнтований граф
        :param vertices: Кількість вершин у графі
        """
        super().__init__(oriented, vertices)  # Виклик конструктора батьківського класу

        # Список навантажень вершин
        self.mData = [self.DEFAULT_VERTEX_DATA] * self.mVertexNumber

    def setData(self, vertex, data):
        """ Встановлення навантаження на вершину
        :param vertex: Вершина графа
        :param data:   Навантаження
        """
        assert 0 <= vertex < self.mVertexNumber
        self.mData[vertex] = data

    def data(self, vertex):
        """ Повертає навантаження заданої вершини графу

        :param vertex: Вершина графа
        :return: Навантаження вершини графа
        """
        assert 0 <= vertex < self.mVertexNumber
        return self.mData[vertex]

    def __str__(self):
        """ Зображення графа разом з усіма вершинами і ребрами у вигляді рядка """

        s = super().__str__() + "\n"
        s += str(self.mData)
        return s


if __name__ == "__main__": # Для тестування

    g = GraphWithData(False, 5)

    g.addEdge(3, 4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)

    print(g)

