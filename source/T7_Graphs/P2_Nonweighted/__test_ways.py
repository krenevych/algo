from random import Random

from source.T7_Graphs.P2_Nonweighted.L4_Ways import waySearch
from source.T7_Graphs.P3_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P3_Weighted.L5_BelmanFordOptimized import BelmanFordOptimized
from source.T7_Graphs.P3_Weighted.L6_Dijkstra import Dijkstra
from source.T7_Graphs.P3_Weighted.__test_weighted import show_way


def showWay(vertices: list, weight, tag):

    if vertices is None:  # шляху не існує
        print(tag, "Шляху не існує! ")
        return

    # виводимо шлях way на екран
    print(tag, "(%d): " % weight, end="")
    for i in range(len(vertices) - 1):
        print(vertices[i], end=" -> ")
    print(vertices[-1])



def inputGraphRandom(vertices, edges):
    """ Ініціалізація графу випадковим чином.

    Заповнює граф вершинами з випадковими позиціями та ребрами з випадковою вагою

    :param graph:    Порожній граф
    :param vertices: Кількість вершин
    :param edges:    Кількість ребер
    :return: None
    """

    graph = GraphForAlgorithms()

    for v in range(vertices + 1):
        graph.addVertex(v)

    for e in range(edges):
        rnd = Random()
        frm = rnd.randint(1, vertices)
        to = rnd.randint(1, vertices)
        if frm != to:
            graph.addEdge(frm, to)
    return graph


if __name__ == "__main__":
    points = 40
    edges = 50

    startV = 1

    g = inputGraphRandom(points, edges)  # Створюємо неорієнтований граф

    # BFS(g, 0)
    #
    # DFS(g, 0)  # запускаємо DFS з вершини 0

    way = waySearch(g, startV, points)
    lenth = 0 if way is None else len(way) - 1
    showWay(way, lenth, "Wave algorithm1                        ")
    #
    # dist = wave(g, 1)
    # print(dist[points])

    print("===================")
    way, way_weight = Dijkstra(g, startV, points)
    show_way(way, way_weight, "Dijkstra algorithm                    ")
    print("===================")
    print("===================")
    way, way_weight = BelmanFordOptimized(g, startV, points)
    show_way(way, way_weight, "Optimization of Bellman-Ford algorithm")
    print("===================")