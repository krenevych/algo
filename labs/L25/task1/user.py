"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
INF = 100000000


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbour = {}  # список (словник ключ_вершини: вага ребра) сусідів
        self.distance = INF

    def __str__(self):
        return str(self.key) + ":" + str(*self.neighbour.keys())


graph = []  # граф, як список вершин


def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph
    for i in range(vertices):
        graph.append(Vertex(i))


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    global graph
    graph[source].neighbour[destination] = weight
    return True


def findDistance(start, end):
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    global graph
    for v in graph:
        v.distance = INF

    graph[start].distance = 0

    for i in range(len(graph) - 1):
        for v in graph:
            for neigb, weight in v.neighbour.items():
                new_dist = v.distance + weight
                if new_dist < graph[neigb].distance:
                    graph[neigb].distance = new_dist

    return graph[end].distance if graph[end].distance < INF else -1
