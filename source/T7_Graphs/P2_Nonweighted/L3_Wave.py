from source.T5_LinearStructure.P2_Queue.L1_Queue import Queue
from source.T7_Graphs.P1_Definitions.L5_Graph import exampleNonorientedHandBook


def wave(graph, start):
    """ Хвильовий алгоритм, що використовує масив
        відстаней від стартової точки до поточної
        для визначення чи була вже відвідана вершина

    :param graph: Граф
    :param start: Вершина з якої починається обхід
    :return: Список відстаней від стартової вершини до кожної вернини графа
    """
    q = Queue()
    q.enqueue(start)

    # Словник, що для всіх вершин містить відстані від стартової вершини start.
    distances = {start: 0}  # Відстань від стартової точки до себе нуль.

    while not q.empty():
        current = q.dequeue()  # Беремо перший елемент з черги
        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if neighbour not in distances:  # які ще не були відвідані
                q.enqueue(neighbour)
                distances[neighbour] = distances[current] + 1

    return distances


if __name__ == "__main__":  # Для тестування
    g = exampleNonorientedHandBook()  # Створюємо неорієнтований граф
    distances = wave(g, 1)
    print(distances)

