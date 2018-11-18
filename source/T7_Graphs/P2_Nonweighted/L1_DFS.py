from source.T7_Graphs.P1_Definitions.L5_Graph import Graph


def DFS(graph, start):
    """ Обхід графа в глибину починаючи з заданої вершини

    :param graph: Граф
    :param start: Вершина з якої відбувається запуск обходу в глибину
    :return: Множина відвіданих вершин
    """

    visited = set()    # відвідані вершини
    __dfs_helper(graph, visited, start)  # запускаємо DFS з вершини start

    return visited

def __dfs_helper(graph, visited, start):
    """ Рекурсивний допоміжний метод, що реалізує обхід графа в глибину

    :param graph:   Граф
    :param visited: Відвідані вершин
    :param start:   Вершина з якої відбувається запуск обходу в глибину
    """
    # print(start, end=" ")    # Опрацьовуємо елемент на вході
    visited.add(start)       # Помічаємо стартовий елемент як відвіданий
    # для всіх сусідів стартового елементу
    for neighbour in graph[start].neighbors():
        if neighbour not in visited:  # які ще не були відвідані
            __dfs_helper(graph, visited, neighbour)  # запускаємо DFS


def exampleNonorientedHandBook2():
    g = Graph()  # Створюємо неорієнтований граф

    g.addEdge(1, 2)  # ребра (1, 2) та (2, 1)
    g.addEdge(1, 3)  # ребра (1, 3) та (1, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(3, 9)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 6)
    g.addEdge(7, 9)
    g.addEdge(8, 9)
    g.addEdge(8, 13)
    g.addEdge(8, 14)
    g.addEdge(8, 15)
    g.addEdge(9, 10)
    g.addEdge(9, 11)
    g.addEdge(9, 12)
    return g

def exampleOrientedHandBook():
    g = Graph(True)  # Створюємо орієнтований граф

    g.addEdge(1, 2)  # ребро (1, 2)
    g.addEdge(1, 3)  # ребро (1, 3)
    g.addEdge(1, 4)  # ребро (1, 4)
    g.addEdge(2, 3)  # ребро (2, 3)
    g.addEdge(2, 5)  # ребро (2, 5)
    g.addEdge(3, 5)  # ребро (3, 5)
    g.addEdge(3, 6)  # ребро (3, 6)
    g.addEdge(4, 3)  # ребро (4, 3)
    g.addEdge(4, 6)  # ребро (4, 6)
    g.addEdge(5, 4)  # ребро (5, 4)
    g.addEdge(5, 6)  # ребро (5, 6)
    return g

if __name__ == "__main__":  # Для тестування

    g = exampleOrientedHandBook()

    DFS(g, 1)
    print()
    DFS(g, 5)
    print()
    DFS(g, 4)
    print()
    DFS(g, 2)
