from source.T5_LinearStructure.P1_Stack.L5_1_Stack import Stack
from source.T7_Graphs.P51.ColorGraph import ColorGraph, BLACK, GRAY

def __helper(graph, vertex, stack):
    """ Рекурсивний допоміжний метод, що реалізує топологічне сотрування
        використовуючи пошук в глибину

    :param graph: Граф
    :param vertex: вершина з якої почитається пошук в глибину
    :param stack: поточний стек відсортовних вершин
    :return: None
    """

    if vertex.color() == BLACK:  # вершина повністю опрацьована
        return

    if vertex.color() == GRAY:   # Істиність цієї умови означає, що знайдено цикл,
        raise Exception          # подальша робота алгоритму не має сенсу

    # print(vertex.key(), " -> GRAY")
    vertex.set_color(GRAY)       # помічаємо вершину сірим кольором, тобто ввійшли в неї
    for neighbour_key in graph[vertex].neighbors():  # для всіх сусідів стартового елементу
        neighbour = graph[neighbour_key]
        __helper(graph, neighbour, stack)  # запускаємо DFS

    # print(vertex.key(), " -> BLACK")
    vertex.set_color(BLACK)           # Помічаємо вершину як опрацьовану (чорним кольором)
    stack.push(vertex.key())  # Вставляємо вершину у список топологічно відсортованих вершин


def topological_sorting(graph):
    """ Функція топологічного сортування вершин графа

    :param graph: граф
    :return: список топологічно відсортованих вершин
    """

    stack = Stack()        # Стек, що буде містити відсортовані елементи
    for vertex in graph:   # для всіх вершин графа
        # запускаємо пошук в глибину
        __helper(graph, vertex, stack)

    # Створюємо список топологічно відсортованих вершин
    sequence = []
    while not stack.empty():
        sequence.append(stack.pop())

    return sequence  # Повертаємо список, що містить відсортовані елементи


##################################################################

if __name__ == "__main__":
    gr = ColorGraph(True)  # Створюємо орієнтований граф

    gr.add_edge(1, 4)
    gr.add_edge(1, 5)
    gr.add_edge(2, 4)
    gr.add_edge(3, 5)
    gr.add_edge(3, 8)
    gr.add_edge(4, 6)
    gr.add_edge(4, 7)
    gr.add_edge(4, 8)
    gr.add_edge(5, 7)
    # gr.add_edge(7, 6)

    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"

    # gr.add_edge(e, f)
    # gr.add_edge(d, g)
    # gr.add_edge(d, e)
    # gr.add_edge(f, g)
    # gr.add_edge(a, b)
    # gr.add_edge(a, c)
    # gr.add_edge(a, d)
    # gr.add_edge(a, e)
    # gr.add_edge(b, d)
    # gr.add_edge(c, d)
    # gr.add_edge(c, e)
    # gr.add_edge(e, g)
    # # gr.add_edge(f, a)

    s = topological_sorting(gr)

    print(*s)