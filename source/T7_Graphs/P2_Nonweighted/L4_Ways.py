import sys

from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.T7_Graphs.P1_Definitions.L5_Graph import exampleNonorientedHandBook
from source.T7_Graphs.P3_Weighted.L8_PlainGraph import PlainGraph, inputGraphWithRandomVertexPositions
from source.utils.benchmark import benchmark


INF = sys.maxsize  # Умовна нескінченність


@benchmark
def waySearch(graph, start, end):
    """ Пошук найкоротшого шляху між двома заданими вершинами графа

    :param graph: Граф
    :param start: Початкова вершина
    :param end:   Кінцева вершина
    :return: список вершин найкоротшого шляху, що сполучає вершини start та end
    """

    assert start != end

    # Словник, що для кожної вершини (ключ) містить ключ вершини з якої прийшли у поточну
    sources = {start: None}  # Для стартової вершини не визначено звідки в неї прийшли.

    q = Queue()           # Створюємо чергу
    q.enqueue(start)      # Додаємо у чергу стартову вершину

    while not q.empty():
        current = q.dequeue()  # Беремо перший елемент з черги
        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if neighbour not in sources:  # які ще не були відвідані
                q.enqueue(neighbour)
                # при цьому для кожної вершини запам'ятовуємо вершину з якої прийшли
                sources[neighbour] = current


    if end not in sources:  # шляху не існує
        return None

    # будуємо шлях за допомогою стеку
    stack = Stack()
    current = end
    while current != start:
        stack.push(current)
        current = sources[current]
    stack.push(current)


    way = []  # Послідовність вершин шляху
    while not stack.empty():
        way.append(stack.pop())

    # Повертаємо шлях
    return way


if __name__ == "__main__":  # Для тестування

    g = exampleNonorientedHandBook()  # Створюємо неорієнтований граф
    way = waySearch(g, 1, 5)
    print(way)

