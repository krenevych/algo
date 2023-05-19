"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""
from labs.L25.task2.PriorityQueue import PriorityQueue

graph = []
INF = 100500

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neigbours = {}
        self.distance = INF
        self.source = None

    def __str__(self):
        return f"{self.key} , dist({self.distance}) : {self.neigbours}"

    def __repr__(self):
        return str(self)

def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph
    graph = []
    for v in range(vertices):
        graph.append(Vertex(v))


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    graph[source].neigbours[destination] = weight


def getWay(start, end):
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    global graph
    vertex = graph[start]
    vertex.distance = 0

    pq = PriorityQueue()
    for v in graph:
        pq.insert(v.key, v.distance)

    while not pq.empty():
        vertex_key = pq.extractMinimum()
        vertex = graph[vertex_key]
        for neig, weight in vertex.neigbours.items():
            new_dist = vertex.distance + weight
            if new_dist < graph[neig].distance:
                graph[neig].distance = new_dist
                graph[neig].source = vertex
                pq.updatePriority(neig, graph[neig].distance)

    if graph[end].source == None:
        return []

    way = []
    cur_vertex = graph[end]
    while cur_vertex is not None:
        way.append(cur_vertex.key)
        cur_vertex = cur_vertex.source
    way = way[::-1]
    return way
