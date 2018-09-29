from source.T7_Graphs.P1.GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P2.BFS import BFS
from source.T7_Graphs.P2.DFS import DFS
from source.T7_Graphs.P2.Ways import waySearch, waySearchByWave


def show_way(vertices: list, weight, tag):

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

    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 0)
    g.add_edge(5, 4)
    g.add_edge(5, 2)
    g.add_edge(6, 7)

    BFS(g, 0)

    DFS(g, 0)  # запускаємо DFS з вершини 0

    way, way_weight = waySearch(g, 0, 7)
    show_way(way, way_weight, "Wave algorithm1                        ")

    way, way_weight = waySearchByWave(g, 0, 3)
    show_way(way, way_weight, "Wave algorithm2                        ")
