from source.T7_Graphs.P1_Definitions.L5_Graph import Graph
from source.T7_Graphs.P2_Nonweighted.L1_DFS import DFS


def __check_connected_helper(graph: Graph):
    """ допоміжний метод, який використовуючи пошук в глибину,
    перевіряє чи існує шлях від вершини 0 до всіх вершин графа

    :param graph: Граф
    :return: True, якщо шлях існує та False, якщо ні
    """

    visited = DFS(graph, 0)

    for v in visited:
        if not v:         # Якщо якась з вершин була не відвідана під час обходу в ширину
            return False  # то граф не є зв'язним

    return True  # якщо не знайдено невідвіданих вершин - граф зв'язний


def checkConnected(graph: Graph):
    """ Перевіряє чи є неорієнтований граф зв'язним, використовуючи пошук в глибину

    :param graph: Граф
    :return: True, якщо граф є зв'язним та False, якщо ні
    """
    assert not graph.mIsOriented     # Перевіряємо, що граф є не орієнтованим
    return __check_connected_helper(graph)


def checkStrongConnected(graph: Graph):
    """ Перевіряє чи є орієнтований граф сильно зв'язним,
    використовується пошук в глибину

    :param graph: Граф
    :return: True, якщо граф є сильно зв'язним та False, якщо ні
    """

    assert graph.mIsOriented  # Перевіряємо, що граф є орієнтованим

    # Перевіряємо перше твердження теореми:
    # 1. З деякої заданої фіксованої вершини існує шлях до всіх вершин графа
    if not __check_connected_helper(graph):
        return False

    # Перевіряємо друге твердження теореми:
    # 2. З кожної вершини графа існує шлях до деякої заданої фіксованої.
    graph_inv = graph.inverse()  # Побудова графу, інвертованого до заданого
    return __check_connected_helper(graph_inv)

