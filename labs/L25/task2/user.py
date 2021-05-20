"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""
from labs.L25.task2.PriorityQueue import PriorityQueue

INF = 100000000


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbour = {}  # список (словник ключ_вершини: вага ребра) сусідів
        self.distance = INF
        self.source = None  # використовується для побудови шляху - вершина з якої ми прийшли у поточну вершину

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
    graph = []
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


def getWay(start, end):
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    global graph
    for v in graph:
        v.distance = INF
        v.source = None

    graph[start].distance = 0
    pq = PriorityQueue()
    for key_ver in range(len(graph)):
        pq.insert(key_ver, graph[key_ver].distance)

    while not pq.empty():
        vert = pq.extractMinimum()

        for neigb, weight in graph[vert].neighbour.items():
            new_dist = graph[vert].distance + weight
            if neigb in pq and new_dist < graph[neigb].distance:
                graph[neigb].distance = new_dist
                graph[neigb].source = vert
                pq.updatePriority(neigb, graph[neigb].distance)

    if graph[end].distance == INF:
        return []

    curr = end
    way = []
    while True:
        way.append(curr)
        if curr == start:
            break
        curr = graph[curr].source

    return way[::-1]
