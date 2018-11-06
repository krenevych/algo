from source.T7_Graphs.P1_Definitions import L5_Graph


class GraphWithData(L5_Graph):
    """ Клас нащадок класу Graph
        Містить поле навантаження вершини
    """

    DEFAULT_VERTEX_DATA = 0  # типове навантаження на вершину

    def __init__(self, oriented: bool = False, vertex_number: int = 20):
        """ Конструктор

        :param oriented: Чи орієнтований граф
        :param vertex_number: Кількість вершин у графі
        """
        super().__init__(oriented, vertex_number)  # Викликаємо конструктор батьківського класу

        # визначаємо список де зберігається навантаження на кожну вершину
        self.mData = [self.DEFAULT_VERTEX_DATA] * self.mVertexNumber

    def setData(self, vertex, data):
        """ Встановлення навантаження на вершину

        :param vertex: Вершина графа
        :param data: Навантаження
        :return: None
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

    g.add_edge(3, 4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)

    print(g)

