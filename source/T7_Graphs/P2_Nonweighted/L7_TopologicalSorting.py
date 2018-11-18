from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.T7_Graphs.P2_Nonweighted.L6_ColorGraph import ColorGraph, BLACK, GRAY


def __dfs_helper(graph, vertex, stack):
    """ Рекурсивний допоміжний метод, що реалізує топологічне сортування
        використовуючи пошук в глибину

    :param graph:  Граф
    :param vertex: вершина з якої почитається пошук в глибину
    :param stack:  поточний стек відсортовних вершин
    :return: None
    """

    if vertex.color() == BLACK:  # вершина повністю опрацьована - вийшли з неї
        return

    if vertex.color() == GRAY:   # Істиність цієї умови означає, що знайдено цикл,
        raise Exception          # подальша робота алгоритму не має сенсу

    # print(vertex.key(), " -> GRAY")
    vertex.setColor(GRAY)       # помічаємо вершину сірим кольором, тобто ввійшли в неї
    for neighbour_key in graph[vertex].neighbors():  # для всіх сусідів стартового елементу
        neighbour = graph[neighbour_key]
        __dfs_helper(graph, neighbour, stack)  # запускаємо DFS

    # Виходимо з вершини
    # print(vertex.key(), " -> BLACK")
    vertex.setColor(BLACK)    # Помічаємо вершину як опрацьовану (чорним кольором)
    stack.push(vertex.key())  # Вставляємо вершину у список топологічно відсортованих вершин


def topological_sorting(graph):
    """ Функція топологічного сортування вершин графа

    :param graph: граф
    :return: список топологічно відсортованих вершин
    """

    stack = Stack()        # Стек, що буде містити відсортовані елементи
    for vertex in graph:   # для всіх вершин графа
        # запускаємо пошук в глибину
        __dfs_helper(graph, vertex, stack)

    # Створюємо список топологічно відсортованих вершин
    sequence = []
    while not stack.empty():
        sequence.append(stack.pop())

    return sequence  # Повертаємо список, що містить відсортовані елементи


##################################################################

if __name__ == "__main__":
    g = ColorGraph(True)  # Створюємо орієнтований граф

    g.addEdge(1, 2)  # ребро (1, 2)
    g.addEdge(1, 3)  # ребро (1, 3)
    g.addEdge(1, 4)  # ребро (1, 4)
    g.addEdge(2, 3)  # ребро (2, 3)
    g.addEdge(2, 5)  # ребро (2, 5)
    g.addEdge(3, 4)  # ребро (3, 4)
    g.addEdge(3, 5)  # ребро (3, 5)
    g.addEdge(3, 6)  # ребро (3, 6)
    g.addEdge(4, 6)  # ребро (4, 6)
    g.addEdge(5, 4)  # ребро (5, 4)
    g.addEdge(5, 6)  # ребро (5, 6)

    s = topological_sorting(g)

    print(*s)