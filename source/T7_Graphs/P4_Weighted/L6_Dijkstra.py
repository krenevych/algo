from source.T7_Graphs.P4_Weighted.L1_VertexForAlgorithms import INF
from source.T6_Trees.P2_BinaryTree.L11_PriorityQueue import PriorityQueue
from source.utils.benchmark import benchmark


@benchmark
def Dijkstra(graph, start, end):
    """ Реалізує алгоритм Дейкстри

    :param graph: Граф
    :param start: Стартова вершина
    :param end: Кінцева вершина
    :return: Кортеж, що містить список вершин - найкоротший шлях, що сполучає вершини start та end та його вагу
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму.
    for vertex in graph:
        vertex.setDistance(INF)  # Відстань для кожної вершини від стартової - нескінченність
        vertex.setSource(None)   # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань у старотовій вершині (тобто від стартової вершини до себе) визначається як 0
    graph[start].setDistance(0)

    pq = PriorityQueue()                  # Створюємо пріоритетну чергу
    pq.insert(start, 0)                   # Додаємо у чергу початкову вершину з нульовим пріоритетом

    # Введемо масив, що буде містити ознаку чи фіксована вже вершина.
    # Ініціалізуємо масив значеннями False (що означає, що вершина не фіксована)
    fixed = [False] * len(graph)

    while not pq.empty():
        vertex_key = pq.extractMinimum()   # Беремо індекс вершини з черги з найвищим пріоритетом
        fixed[vertex_key] = True           # та позначаємо її як фіксавану
        vertex = graph[vertex_key]         # Беремо вершину за індексом

        if vertex_key == end:              # Якщо поточний елемент є шуканим
            break                          # пошук завершено

        for neighbor_key in vertex.neighbors():    # Для всіх сусідів (за ключами) поточної вершини
            if fixed[neighbor_key]:                # які ще не були фіксовані
                continue

            neighbour = graph[neighbor_key]                 # Беремо вершину-сусіда за ключем
            # Обчислюємо потенційну відстань у вершині-сусіді
            newDist = vertex.distance() + vertex.weight(neighbor_key)
            # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
            if newDist < neighbour.distance():
                # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                neighbour.setDistance(newDist)
                # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї
                neighbour.setSource(vertex_key)

                if neighbor_key in pq:   # Якщо вершина сусід міститься у черзі
                    # перераховуємо її пріоритет в черзі
                    pq.updatePriority(neighbor_key, newDist)
                else:
                    # або додаємо елемент до черги, якщо його там ще немає.
                    pq.insert(neighbor_key, newDist)

    return graph.constructWay(start, end)    # Повертаємо шлях та його вагу
