from source.T5_LinearStructure.P42_Queue.Queue import Queue
from source.T7_Graphs.P51.GraphForAlgorithms import GraphForAlgorithms

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


def wave2(graph: GraphForAlgorithms, start: int):

    """ Функція, що запускає хвильовий алгоритм.
        Використовує граф класу GraphForAlgorithms, вершини якого містять допоміжну інформацію.
        Функція модифікує вхідний граф, так, що в результаті його всі вершини
        містять інформацію про найкоротшу відстань від заданої стартової вершини.

    :param graph: Граф, вершини якого містять відстань від початкової вершини
    :param start: Стартова вершина, тобто з якої починається робота хвильового алгоритму
    :return: None
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму.
    for vertex in graph:
        vertex.set_unvisited()   # вершина ще не була відвідана

    # Відстань у старотовій вершині (тобто від стартової вершини до себе) визначається як 0
    graph[start].set_distance(0)

    q = Queue()       # Створюємо чергу
    q.enqueue(start)  # Додаємо у чергу початкову вершину

    while not q.empty():
        vertex_key = q.dequeue()   # Беремо перший елемент з черги
        vertex = graph[vertex_key]  # Беремо вершину за індексом

        # Для всіх сусідів (за ключами) поточної вершини
        for neighbor_key in vertex.neighbors():
            neighbour = graph[neighbor_key]   # Беремо вершину-сусіда за ключем
            if not neighbour.visited():       # Якщо сусід не був відвіданий
                q.enqueue(neighbor_key)       # додаємо його до черги
                neighbour.set_distance(vertex.distance() + 1)  # Встановлюємо значення відстані у вершині-сусіді
                                                               # значенням на 1 більшии ніж у поточній вершині
