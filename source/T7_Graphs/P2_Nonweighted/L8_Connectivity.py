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

