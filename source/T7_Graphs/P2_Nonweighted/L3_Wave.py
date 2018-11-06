from source.T5_LinearStructure.P2_Queue.Queue import Queue


def wave(graph, start):
    """ Хвильовий алгоритм

    :param graph: Граф
    :param start: Вершина з якої починається обхід
    :return: Список відстаней від стартової верниши до кожної вернини графа
    """
    # Введемо масив, що буде містити ознаку чи відвідали вже вершину.
    # Ініціалізуємо масив значеннями False (тобто відвідали)
    visited = [False] * len(graph)

    # Введемо масив, що буде містити
    # відстані від стартової вершини start.
    # Ініціалізуємо масив значеннями -1 (тобто нескінченність)
    distances = [-1] * len(graph)

    q = Queue()  # Створюємо чергу

    q.enqueue(start)  # Додаємо у чергу стартову вершину
    visited[start] = True  # та позначаємо її як відвідану
    distances[start] = 0  # Відстань від стартової точки до себе нуль.

    while not q.empty():

        current = q.dequeue()  # Беремо перший елемент з черги

        # Тут Опрацьовуємо взятий елемент, за необхідності

        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if not visited[neighbour]:  # які ще не були відвідані
                q.enqueue(neighbour)
                visited[neighbour] = True
                # Встановлюємо відстань на одиницю більшу ніж для поточної
                distances[neighbour] = distances[current] + 1

    # Повертаємо масив відстаней від start до всіх вершин графа
    return distances


def wave1(graph, start):
    """ Хвильовий алгоритм, що використовує масив
        відстаней від стартової точки до поточної
        для визначення чи була вже відвідана вершина

    :param graph: Граф
    :param start: Вершина з якої починається обхід
    :return: Список відстаней від стартової верниши до кожної вернини графа
    """
    q = Queue()

    q.enqueue(start)

    # Введемо масив, що буде містити
    # відстані від стартової вершини start.
    # Ініціалізуємо масив значеннями -1 (тобто нескінченність)
    distances = [-1] * len(graph)
    distances[start] = 0  # Відстань від стартової точки до себе нуль.

    while not q.empty():

        current = q.dequeue()  # Беремо перший елемент з черги

        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if distances[neighbour] == -1:  # які ще не були відвідані
                q.enqueue(neighbour)
                distances[neighbour] = distances[current] + 1

    return distances

