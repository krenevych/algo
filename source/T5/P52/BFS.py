from source.T4.P42_Queue.Queue import Queue


def BFS(graph, start):
    """ Обхід графа в ширину починаючи з заданої вершини

    :param graph: Граф
    :param start: Вершина з якої відбувається запуск обходу в ширину
    :return: Список, i-й елемент якого містить позначку чи була відвідана i-та вершина
    """

    # Введемо масив, що буде містити ознаку чи відвідали вже вершину.
    # Ініціалізуємо масив значеннями False (тобто не відвідали)
    visited = [False] * len(graph)

    q = Queue()            # Створюємо чергу
    q.enqueue(start)       # Додаємо у чергу стартову вершину
    visited[start] = True  # та позначаємо її як відвідану

    while not q.empty():       # Поки черга не порожня
        current = q.dequeue()  # Беремо перший елемент з черги

        print(current)         # Опрацьовуємо взятий елемент

        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if not visited[neighbour]:  # які ще не були відвідані
                q.enqueue(neighbour)
                visited[neighbour] = True # Помічаємо як відвідану

    return visited


