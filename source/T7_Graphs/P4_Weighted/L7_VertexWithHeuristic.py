from source.T7_Graphs.P1_Definitions.L4_Vertex import Vertex
from source.T7_Graphs.P4_Weighted.L1_VertexForAlgorithms import VertexForAlgorithms


class VertexWithHeuristic(VertexForAlgorithms):
    """ Клас, що є розширенням графа VertexForAlgorithms

     Використовується у алгоритмі А*.
     Міститть значення евристичної функції (евристику), що необхідна для реалізації алгоритму А*. """

    def __init__(self, key):
        """ Конструктор вершини

        :param key: Ключ вершини
        """
        super().__init__(key)
        self.mHeuristicValue = 0   # Значення еврестичної функції (евристика)

    def heuristic(self):
        """ Значення евристики у поточній вершині

        :return: евристику у поточній вершині
        """
        return self.mHeuristicValue

    def calculateHeuristic(self, other):
        """ Допоміжний метод, що встанолює значення евристичної функції у вершині.

        Вибирається спеціальним чином з аналізу властивостей графу (наприклад в залежності від топології графу).
        Тут евристика визначається як геометрична відстань (по прямій лінії) між двома вершинами у графі

        :param other: Інша вершина графа (у алгоритмі А* це стартова вершина з якої починається пошук шляху)
        :return: None.
        """
        position = self.mData

        if isinstance(other, Vertex):
            dest_position = other.data()
        else:
            dest_position = other

        assert position is not None and dest_position is not None

        self.mHeuristicValue = (((dest_position[0] - position[0]) ** 2) + ((dest_position[1] - position[1]) ** 2)) ** 0.5

    def __str__(self):
        """ Зображення вершини у вигляді рядка у разом з усіма її сусідами """
        return str(self.mKey) + ": Data = " + str(self.data()) + "  Dist = " + str(self.mDistance) + "  Heuristic = " + str(self.mHeuristicValue) + "  From: " + str(self.mSource) + ' connected: ' + str(self.mNeighbors)

