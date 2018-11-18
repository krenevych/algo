from source.T7_Graphs.P1_Definitions.L5_Graph import Graph
from source.T7_Graphs.P2_Nonweighted.L8_Connectivity import __check_connected_helper


def checkStrongConnected(graph: Graph):
    """ Перевіряє чи є орієнтований граф сильно зв'язним,
    використовується пошук в глибину

    :param graph: Граф
    :return: True, якщо граф є сильно зв'язним та False, якщо ні
    """

    assert graph.mIsOriented  # Перевіряємо, що граф є орієнтованим

    # Перевіряємо перше твердження теореми:
    # 1. З деякої заданої фіксованої вершини існує шлях до всіх вершин графа
    if not __check_connected_helper(graph, 1):
        return False

    # Перевіряємо друге твердження теореми:
    # 2. З кожної вершини графа існує шлях до деякої заданої фіксованої.
    graph_inv = graph.transpose()  # Побудова графу, транспонованого до заданого
    return __check_connected_helper(graph_inv, 1)


if __name__ == "__main__":  # Для тестування

    g = Graph(True)  # Створюємо орієнтований граф

    g.addEdge(1, 2)  # ребро (1, 2)
    g.addEdge(1, 3)  # ребро (1, 3)
    g.addEdge(2, 3)  # ребро (2, 3)
    g.addEdge(2, 5)  # ребро (2, 5)
    g.addEdge(3, 4)  # ребро (3, 4)
    g.addEdge(3, 5)  # ребро (3, 5)
    g.addEdge(3, 6)  # ребро (3, 6)
    g.addEdge(4, 1)  # ребро (1, 4)
    g.addEdge(5, 4)  # ребро (5, 4)
    g.addEdge(5, 6)  # ребро (5, 6)
    g.addEdge(6, 4)  # ребро (4, 6)

    print(checkStrongConnected(g))