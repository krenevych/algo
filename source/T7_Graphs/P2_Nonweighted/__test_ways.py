from source.T7_Graphs.P3_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P2_Nonweighted.L2_BFS import BFS
from source.T7_Graphs.P2_Nonweighted.L1_DFS import DFS
from source.T7_Graphs.P2_Nonweighted.L4_Ways import waySearch


def showWay(vertices: list, weight, tag):

    if vertices is None:  # шляху не існує
        print(tag, "Шляху не існує! ")
        return

    # виводимо шлях way на екран
    print(tag, "(%d): " % weight, end="")
    for i in range(len(vertices) - 1):
        print(vertices[i], end=" -> ")
    print(vertices[-1])


if __name__ == "__main__":
    g = GraphForAlgorithms(False)  # Створюємо орієнтований граф

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)
    g.addEdge(6, 7)

    BFS(g, 0)

    DFS(g, 0)  # запускаємо DFS з вершини 0

    way, way_weight = waySearch(g, 0, 5)
    showWay(way, way_weight, "Wave algorithm1                        ")

