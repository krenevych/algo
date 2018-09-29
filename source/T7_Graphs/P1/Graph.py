from random import Random

from source.T7_Graphs.P1.Vertex import Vertex


class Graph:
    """ Граф, що задається списком суміжних вершин """

    def __init__(self, oriented=False):
        """ Конструктор графа

        :param oriented: Чи орієнтований граф
        """
        self.mIsOriented = oriented    # Поле чи орієнтований граф
        self.mVertexNumber = 0         # Лічильник вершин у графі
        self.mVertices = {}            # Список (словник) вершин у графі у вигляді пар (ключ: вершина)

    def add_vertex(self, vertex):
        """ Додає вершину у граф, якщо така вершина не міститься у ньому

        :param vertex: ключ (тобто ім'я) нової вершини
        :return: True, якщо вершина успішно додана
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = Vertex(vertex)  # створюємо нову вершину з іменем Vertex
        self.mVertices[vertex] = new_vertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1                  # Збільшуємо лічильник вершин у графі
        return True

    def get_vertex(self, vertex):
        """ Повертає вершину графу, якщо така вершина міститься у графі

        :param vertex: ключ (тобто ім'я) вершини
        :return: Вершина графа
        """
        assert vertex in self

        # Визначаємо ключ вершини, якщо це необхідно
        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.mVertices[key]

    def vertices(self):
        """ Повертає список всіх вершин у графі"""
        return self.mVertices

    def add_edge(self, source, destination, weight=1):
        """ Додавання ребра з кінцями в точках source та destination з вагою weight

        :param source: Перша вернина
        :param destination: Друга вершина
        :param weight: Вага ребра
        :return: None
        """
        if source not in self:            # Якщо вершина source ще не міститься у графі
            self.add_vertex(source)       # додаємо вершину source
        if destination not in self:       # Якщо вершина destination ще не міститься у графі
            self.add_vertex(destination)  # додаємо вершину destination

        # Встановлюємо зв'язок (тобто ребро) між вершинами source та destination
        self[source].add_neighbor(destination, weight)

        if not self.mIsOriented:  # Якщо граф не орієнтований, то треба додати зворотній зв'язок
            self.mVertices[destination].add_neighbor(source, weight)

    def set_data(self, vertex, data):
        """ Встановлення навантаження вершини

        :param vertex: ключ вершини або вершина графа
        :param data: навантаження
        :return: None
        """
        assert vertex in self # Перевірка чи міститься вершина в графі
        self[vertex].set_data(data)

    def get_data(self, vertex):
        """ Повертає навантаження вершини

        :param vertex: Вершина або її ключ
        :return: Навантаження вершини
        """
        assert vertex in self  # Перевірка чи міститься вершина в графі
        return self[vertex].data()

    def inverse(self):
        """ Будує граф інвертований до заданого

        :return: Новий граф, що є інвертованим до заданого
        """

        g_inv = Graph(self.mIsOriented)
        for vertex in self:
            for neighbor_key in vertex.neighbors():    # Для всіх сусідів (за ключами) поточної вершини
                g_inv.add_edge(neighbor_key, vertex.key())

        return g_inv

    def __contains__(self, vertex):
        """Перевизначення оператора in - перевіряє чи міститься вершина у графі

        :param vertex: Вершина або її ключ
        :return: True, якщо задана вершина міститься у графі
        """
        if isinstance(vertex, Vertex):  # Якщо Vertex - вершина (не ім'я)
            return vertex.key() in self.mVertices
        else:                           # Якщо Vertex - ім'я (ключ) вершини
            return vertex in self.mVertices

    def __iter__(self):
        """ Ітератор для послідовного проходження всіх вершин у графі """
        return iter(self.mVertices.values())

    def __len__(self):
        """ Перевизначення методу len() як кількість вершин у графі

        :return: кількість вершин у графі
        """
        return self.mVertexNumber

    def __str__(self):
        """ Зображення графа разом з усіма вершинами і ребрами у вигляді рядка """
        s = ""
        for vertex in self:
            s = s + str(vertex) + "\n"
        return s

    def __getitem__(self, vertex):
        return self.get_vertex(vertex)


def inputRandomGraph(graph, vertices, edges):
    """ Ініціалізація графу випадковим чином

    :param graph: Порожній граф
    :param vertices: Кількість вершин
    :param edges: Кількість ребер
    :return: None
    """

    graph.add_vertex(0)

    for e in range(edges):
        rnd = Random()
        frm = rnd.randint(0, vertices)
        to = rnd.randint(0, vertices)
        if frm != to:
            weight = rnd.randint(1, 15)
            graph.add_edge(frm, to, weight)

            # FOR DEBUG
            # print("gr.addEdge(%d, %d, %d)" % (frm, to, weight))

    print("=========================")

def inputConcreteGraph(g):
    """ Ініціалізація графу

    :param g: Порожній граф
    :return: None
    """
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

def inputConcreteGraph1(gr):
    """ Ініціалізація графу

    :param gr: Порожній граф
    :return: None
    """
    gr.add_edge(0, 2, 14)
    gr.add_edge(0, 3, 13)
    gr.add_edge(0, 5, 2)
    gr.add_edge(0, 7, 3)

    gr.add_edge(1, 2, 12)
    gr.add_edge(1, 7, 11)

    gr.add_edge(2, 0, 1)
    gr.add_edge(2, 3, 3)
    gr.add_edge(2, 4, 10)
    gr.add_edge(2, 7, 2)
    gr.add_edge(2, 8, 10)
    gr.add_edge(2, 10, 13)

    gr.add_edge(3, 0, 13)
    gr.add_edge(3, 2, 10)

    gr.add_edge(4, 5, 2)
    gr.add_edge(4, 6, 15)
    gr.add_edge(4, 9, 7)

    gr.add_edge(5, 0, 13)
    gr.add_edge(5, 8, 7)
    gr.add_edge(5, 9, 4)

    gr.add_edge(6, 7, 8)
    gr.add_edge(6, 10, 2)

    gr.add_edge(7, 1, 1)
    gr.add_edge(7, 2, 8)
    gr.add_edge(7, 3, 7)
    gr.add_edge(7, 5, 1)
    gr.add_edge(7, 6, 13)

    gr.add_edge(8, 3, 14)
    gr.add_edge(8, 4, 15)
    gr.add_edge(8, 9, 15)

    gr.add_edge(9, 2, 8)
    gr.add_edge(9, 5, 6)

    gr.add_edge(10, 1, 14)
    gr.add_edge(10, 4, 10)
    gr.add_edge(10, 5, 11)

    print("=========================")

def inputConcreteGraph2(gr):
    """ Ініціалізація графу

    :param gr: Порожній граф
    :return: None
    """
    gr.add_edge(0, 2, 3)
    gr.add_edge(0, 3, 14)
    gr.add_edge(0, 5, 7)
    gr.add_edge(0, 6, 2)

    gr.add_edge(1, 4, 13)
    gr.add_edge(1, 6, 3)
    gr.add_edge(1, 7, 8)

    gr.add_edge(2, 0, 2)
    gr.add_edge(2, 4, 9)
    gr.add_edge(2, 6, 10)
    gr.add_edge(2, 7, 15)

    gr.add_edge(3, 0, 4)
    gr.add_edge(3, 1, 6)
    gr.add_edge(3, 4, 3)
    gr.add_edge(3, 5, 11)
    gr.add_edge(3, 6, 9)
    gr.add_edge(3, 7, 3)

    gr.add_edge(4, 5, 12)
    gr.add_edge(4, 7, 11)

    gr.add_edge(5, 1, 5)
    gr.add_edge(5, 4, 9)

    gr.add_edge(6, 1, 3)
    gr.add_edge(6, 0, 1)
    gr.add_edge(6, 7, 14)

    gr.add_edge(7, 1, 14)
    gr.add_edge(7, 2, 14)

def inputConcreteGraph3(gr):
    """ Ініціалізація графу

    :param gr: Порожній граф
    :return: None
    """
    gr.add_edge(0, 1)
    gr.add_edge(1, 2)
    gr.add_edge(2, 3)
    gr.add_edge(3, 0)
    # g_0.add_edge(0, 3)
    gr.add_edge(4, 1)
    # g_0.add_edge(2, 4)
    gr.add_edge(4, 2)

def inputConcreteGraph4(gr):
    """ Ініціалізація графу

    :param gr: Порожній граф
    :return: None
    """
    gr.add_edge(0, 2)
    gr.add_edge(0, 4)

    # gr.add_edge(1, 3)

    gr.add_edge(2, 3)
    gr.add_edge(2, 5)
    gr.add_edge(2, 6)

    gr.add_edge(3, 0)
    gr.add_edge(3, 4)
    gr.add_edge(3, 5)

    gr.add_edge(4, 2)
    gr.add_edge(4, 5)

    gr.add_edge(5, 0)
    gr.add_edge(5, 2)
    gr.add_edge(5, 3)
    gr.add_edge(5, 4)

    gr.add_edge(6, 1)
    gr.add_edge(6, 2)
    gr.add_edge(6, 4)

    # 0: {2, 4}
    # 1: {3}
    # 2: {3, 5, 6}
    # 3: {0, 4, 5}
    # 4: {2, 5}
    # 5: {0, 2, 3, 4}
    # 6: {1, 2, 4}

def inputGraphNet(gr):
    """ Ініціалізація графу-мережі, тобто графу, що немає циклів та має одне джерело та один сток

    :param gr: Порожній граф
    :return: None
    """
    gr.add_edge(0, 1)
    gr.add_edge(0, 2)
    gr.add_edge(0, 3)

    gr.add_edge(1, 4)
    gr.add_edge(1, 5)
    gr.add_edge(2, 5)
    gr.add_edge(3, 5)
    gr.add_edge(3, 6)

    gr.add_edge(4, 7)
    gr.add_edge(4, 8)
    gr.add_edge(5, 7)
    gr.add_edge(5, 8)
    gr.add_edge(5, 9)
    gr.add_edge(6, 8)
    gr.add_edge(6, 9)

    gr.add_edge(7, 10)
    gr.add_edge(8, 10)
    gr.add_edge(9, 10)

    gr.add_edge(10, 0)

    # gr.add_edge(1, 3)

    gr.add_edge(2, 3)
    gr.add_edge(2, 5)
    gr.add_edge(2, 6)

    gr.add_edge(3, 0)
    gr.add_edge(3, 4)
    gr.add_edge(3, 5)

    gr.add_edge(4, 2)
    gr.add_edge(4, 5)

    gr.add_edge(5, 0)
    gr.add_edge(5, 2)
    gr.add_edge(5, 3)
    gr.add_edge(5, 4)

    gr.add_edge(6, 1)
    gr.add_edge(6, 2)
    gr.add_edge(6, 4)


if __name__ == "__main__":  # Для тестування

    g = Graph(True)  # Створюємо орієнтований граф

    # inputConcreteGraph2(g)

    points = 10
    edges = 20
    inputRandomGraph(g, points, edges)

    print(g)