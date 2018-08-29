def __dfs_helper(graph, visited, start):
    """ Рекурсивний допоміжний метод, що реалізує обхід графа в глибину

    :param graph: Граф
    :param visited: Допоміжний список, i-й елемент якого містить позначку чи була відвідана i-та вершина
    :param start: Вершина з якої відбувається запуск обходу в глибину
    :return: None
    """
    # print(start, end=" ")  # Опрацьовуємо елемент на вході
    visited[start] = True    # Помічаємо стартовий елемент як відвіданий
    # для всіх сусідів стартового елементу
    for neighbour in graph[start].neighbors():
        if not visited[neighbour]:  # які ще не були відвідані
            __dfs_helper(graph, visited, neighbour)  # запускаємо DFS
    # print(start, end=" ")  # Опрацьовуємо елемент на виході

def DFS(graph, start):
    """ Обхід графа в глибину починаючи з заданої вершини

    :param graph: Граф
    :param start: Вершина з якої відбувається запуск обходу в глибину
    :return: Список, i-й елемент якого містить позначку чи була відвідана i-та вершина
    """
    # Створюємо список відвіданих вершин, які
    # ініціалізуються значенням False
    visited = [False] * len(graph)
    __dfs_helper(graph, visited, start)  # запускаємо DFS з вершини 0

    return visited
