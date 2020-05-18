from source.T7_Graphs.P4_Weighted.L1_VertexForAlgorithms import INF


def BelmanFordClasical(graph, start):
    """ Класичний алгоритм Беллмана-Форда для графів, що можуть мати цикли від'ємної ваги
        Перевіряє чи має граф цикли від'ємної ваги

    :param graph: Граф
    :param start: Стартова вершина
    :return: False, якщо граф не містить циклів від'ємної ваги
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму
    for vertex in graph:
        vertex.setDistance(INF)  # Відстань для кожної вершини від стартової ставиться як нескінченність

    # Відстань від першої вершини до неї ж визначається як 0
    graph[start].setDistance(0)
    for i in range(len(graph) - 1):
        for vertex in graph:                             # Для всіх вершин графу
            for neighbor_key in vertex.neighbors():      # Для всіх сусідів (за ключами) поточної вершини
                neighbour = graph[neighbor_key]          # Беремо вершину-сусіда за індексом
                newDist = vertex.distance() + vertex.weight(neighbor_key)  # Обчислюємо потенційну відстань у вершині-сусіді
                if newDist < neighbour.distance():       # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbour.setDistance(newDist)      # Змінюємо поточне значення відстані у вершині-сусіді обчисленим

    # Перевірка на наявність циклів з від'ємною вагою
    # Тут фактично здійсюється ще одна ітерація циклу і якщо у одній з вершин знайдена відстань зменшиться,
    # то це і означатиме, що знайдено цикл від'ємної ваги.
    for vertex in graph:                            # Для всіх вершин графу
        for neighbor_key in vertex.neighbors():     # Для всіх сусідів (за ключами) поточної вершини
            neighbour = graph[neighbor_key]         # Беремо вершину-сусіда за індексом
            newDist = vertex.distance() + vertex.weight(neighbor_key)  # Обчислюємо потенційну відстань у вершині-сусіді
            if newDist < neighbour.distance():       # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                return True                          # Знайдено цикл від'ємної ваги.

    return False  # Граф не місіить циклів від'ємної ваги.
