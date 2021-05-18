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


def getWay(start, end):
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    global graph
    for v in graph:
        v.distance = INF

    graph[start].distance = 0
    pq = PriorityQueue()
    for key_ver in range(len(graph)):
        pq.insert(key_ver, graph[key_ver].distance)

    fixed = set()  # список фіксованих(оброблених) вершин

    while not pq.empty():
        vert = pq.extractMinimum()
        fixed.add(vert)

        for neigb, weight in graph[vert].neighbour.items():
            if neigb in fixed:
                continue

            new_dist = graph[vert].distance + weight
            if new_dist < graph[neigb].distance:
                graph[neigb].distance = new_dist
                pq.updatePriority(neigb, graph[neigb].distance)

    dist = graph[end].distance
    return None
