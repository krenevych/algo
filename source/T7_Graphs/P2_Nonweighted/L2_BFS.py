from source.T5_LinearStructure.P2_Queue.L1_Queue import Queue
from source.T7_Graphs.P1_Definitions.L5_Graph import exampleNonorientedHandBook


def BFS(graph, start):
    """ Обхід графа в ширину починаючи з заданої вершини

    :param graph: Граф
    :param start: Вершина з якої відбувається запуск обходу в ширину
    :return: Список (множину) відвіданих вершин
    """

    q = Queue()          # Створюємо чергу
    q.enqueue(start)     # Додаємо у чергу стартову вершину
    visited = set()      # відвідані вершини
    visited.add(start)   # позначаємо початкову вершину як відвідану

    while not q.empty():       # Поки черга не порожня
        current = q.dequeue()  # Беремо перший елемент з черги

        print(current)         # Опрацьовуємо взятий елемент

        # Додаємо в чергу всіх сусідів поточного елементу
        for neighbour in graph[current].neighbors():
            if neighbour not in visited:  # які ще не були відвідані
                q.enqueue(neighbour)
                visited.add(neighbour)  # Помічаємо як відвідану

    return visited


if __name__ == "__main__":  # Для тестування
    g = exampleNonorientedHandBook()  # Створюємо неорієнтований граф
    BFS(g, 1)