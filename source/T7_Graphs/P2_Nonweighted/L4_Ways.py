import sys

from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.utils.benchmark import benchmark


INF = sys.maxsize  # Умовна нескінченність


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
