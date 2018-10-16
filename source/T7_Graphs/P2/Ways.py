from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.T7_Graphs.P1.GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P1.VertexForAlgorithms import INF
from source.utils.benchmark import benchmark


@benchmark
def waySearch(graph, start, end):
    """ Пошук найкоротшого шляху між двома заданими вершинами графа

    :param graph: Граф
    :param start: Початкова вершина
    :param end: Кінцева вершина
    :return: Кортеж, що містить список вершин - найкоротший шлях, що сполучає вершини start та end та його вагу
    """

    assert start != end

    distances = [-1] * len(graph)   # Масив відстаней
    sources = [None] * len(graph)     # Масив вершин звідки прийшли

    q = Queue()           # Створюємо чергу
    q.enqueue(start)      # Додаємо у чергу стартову вершину
    distances[start] = 0  # Відстань від стартової точки до себе нуль.

    while not q.empty():

        current = q.dequeue()  # Беремо перший елемент з черги

        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if distances[neighbour] == -1:  # які ще не були відвідані
                q.enqueue(neighbour)
                distances[neighbour] = distances[current] + 1
                sources[neighbour] = current  # Вказуємо для сусіда neighbour,
                                              # що ми прийшли з вершини current

    if sources[end] is None:  # шляху не існує
        return None, INF

    # будуємо шлях за допомогою стеку
    stack = Stack()
    current = end
    while True:
        stack.push(current)
        if current == start:
            break
        current = sources[current]

    way = []  # Послідовність вершин шляху
    while not stack.empty():
        way.append(stack.pop())

    # Повертаємо шлях та його довжину
    return way, distances[end]

@benchmark
def waySearchByWave(graph: GraphForAlgorithms, start: int, end: int):
    """ Пошук найкоротшої відстані, використовуючи хвильовий алгоритм

    :param graph: Граф
    :param start: Початкова вершина
    :param end:   Кінцева вершина
    :return: Кортеж, що містить список вершин - найкоротший шлях, що сполучає вершини start та end та його вагу
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму.
    for vertex in graph:
        vertex.set_unvisited()   # вершина ще не була відвідана
        vertex.set_source(None)  # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань у старотовій вершині (тобто від стартової вершини до себе) визначається як 0
    graph[start].set_distance(0)

    q = Queue()       # Створюємо чергу
    q.enqueue(start)  # Додаємо у чергу початкову вершину

    while not q.empty():
        vertex_key = q.dequeue()    # Беремо перший елемент з черги
        vertex = graph[vertex_key]  # Беремо вершину за індексом

        # Для всіх сусідів (за ключами) поточної вершини
        for neighbor_key in vertex.neighbors():
            neighbour = graph[neighbor_key]   # Беремо вершину-сусіда за ключем
            if not neighbour.visited():       # Якщо сусід не був відвіданий
                neighbour.set_distance(vertex.distance() + 1)  # Встановлюємо значення відстані у вершині-сусіді
                                                               # значенням на 1 більшии ніж у поточній вершині
                neighbour.set_source(vertex_key)               # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї
                q.enqueue(neighbor_key)       # додаємо сусіда до черги

    return graph.construct_way(start, end)    # Повертаємо шлях та його вагу