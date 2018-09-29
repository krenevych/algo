import sys

from source.T7_Graphs.P1.Vertex import Vertex

INF = sys.maxsize  # Умовна нескінченність

class VertexForAlgorithms(Vertex):
    """ Клас, що є розширенням класу для вершини графа

        Використовується у алгоритмах Белмана-Форда, Дейкстри, А*...
        Міститть додаткову технічну інформацію, що необхідна для реалізації щих алгоритмів
     """

    def __init__(self, key):
        """ Конструктор створення вершини

        :param key: Ключ вершини
        """
        super().__init__(key)

        """ Відтань - додаткове навантаження на вершину - величина найкоротшого шляху 
            від деякої фіксованої вершини до поточної вершини графа.
            Використовується для хвильового алгоритму, алгоритмів Дейкстри, Белмана-Форда та ін. """
        self.mDistance = INF  # До початку роботи алгортиму вважаємо, що вона є несінченністю!

        """ Джерело - додаткове навантаження на вершину -
            вершина з якої прийшли по найкорошому шляху 
            у поточну вернишу на деякому кроці алгоритму """
        self.mSource = None   # До початку роботи алгортиму вважаємо, що вона є невизначеною

    def set_distance(self, distance):
        """ Встановлює відстань для поточної вершини

        :param distance: Нова відстань
        :return: None
        """
        self.mDistance = distance

    def distance(self):
        """ Повератє поточну відстань у вершині

        :return: Відстань у вершині
        """
        return self.mDistance

    def set_source(self, source):
        """ Встанолює джерело для поточної вершини

        :param source: Нове джерело вершини
        :return: None
        """
        self.mSource = source

    def source(self):
        """ Повертає джерело для поточної вершини

        :return: Джерело поточної вершини
        """
        return self.mSource

    def visited(self):
        """ Чи відвідана вершина на поточному кроці алгоритму
        Якщо вершина була принаймні один раз відвідана, то відстань у ній менша за нескінченність

        :return: True, якщо вершина була відвідана на поточному кроці алгоритму
        """
        return self.mDistance != INF

    def set_unvisited(self):
        """ Встановлює відстань у поточній вершині як нескінченність

        :return: None
        """
        self.mDistance = INF

    def __str__(self):
        """ Зображення вершини у вигляді рядка у разом з усіма її сусідами """
        return str(self.mKey) + ": Data = " + str(self.data()) + "  Dist = " + str(self.mDistance) + "  From: " + str(self.mSource) + ' connected: ' + str(self.mNeighbors)
        # return str(self.mId) + ": Data=" + str(self.getData())

