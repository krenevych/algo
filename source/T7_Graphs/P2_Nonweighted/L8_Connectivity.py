from source.T7_Graphs.P1_Definitions.L5_Graph import Graph
from source.T7_Graphs.P2_Nonweighted.L1_DFS import DFS


def __check_connected_helper(graph: Graph, start):
    """ допоміжний метод, який використовуючи пошук в глибину,
    перевіряє чи існує шлях від вершини start до всіх вершин графа

    :param graph: Граф
    :param start: Початкова вершина графа
    :return: True, якщо шлях існує та False, якщо ні
    """

    visited = DFS(graph, start)

    for v in graph.vertices():
        if v not in visited:  # Якщо якась з вершин була не відвідана під час обходу в глибину
            return False      # то граф не є зв'язним

    return True  # якщо не знайдено невідвіданих вершин - граф зв'язний


def checkConnected(graph: Graph):
    """ Перевіряє чи є неорієнтований граф зв'язним

    :param graph: Граф
    :return: True, якщо граф є зв'язним та False, якщо ні
    """
    assert not graph.mIsOriented     # Перевіряємо, що граф є не орієнтованим
    return __check_connected_helper(graph, 1)


if __name__ == "__main__":

    g = Graph()  # Створюємо неорієнтований граф

    g.addEdge(1, 2)  # ребро (1, 2)
    g.addEdge(1, 3)  # ребро (1, 3)
    g.addEdge(1, 4)  # ребро (1, 4)
    g.addEdge(2, 3)  # ребро (2, 3)
    g.addEdge(2, 5)  # ребро (2, 5)
    g.addEdge(3, 4)  # ребро (3, 4)
    g.addEdge(3, 5)  # ребро (3, 5)
    g.addEdge(3, 6)  # ребро (3, 6)
    g.addEdge(4, 6)  # ребро (4, 6)
    g.addEdge(5, 4)  # ребро (5, 4)
    g.addEdge(5, 6)  # ребро (5, 6)

    print(checkConnected(g))