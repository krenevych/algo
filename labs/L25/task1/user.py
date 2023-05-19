"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
graph = []
INF = 100500

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neigbours = {}
        self.distance = INF

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
    pass


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    # print("addEdge: ", source, destination, weight)
    graph[source].neigbours[destination] = weight
    pass

def findDistance(start, end):
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    global graph
    vertex = graph[start]
    vertex.distance = 0

    for i in range(len(graph) - 1):
        for vertex in graph:
            for neig, weight in vertex.neigbours.items():
                new_dist = vertex.distance + weight
                if new_dist < graph[neig].distance:
                    graph[neig].distance = new_dist
                pass
    dist = graph[end].distance
    return dist if dist < INF else -1
