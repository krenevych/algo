from source.T7_Graphs.P1_Definitions.L5_Graph import Graph


def __dfs_helper(graph, visited, start, connected_component):
    """ Рекурсивний допоміжний метод, що реалізує обхід графа в глибину
    При цьому, для відвіданих вершин зберігається інформація
    про їхні компоненти зв'язності

    :param graph:   Граф
    :param visited: Словник відвіданих вершин
    :param start:   Вершина з якої відбувається запуск обходу в глибину
    :param connected_component: Номер поточної компоненти зв'язності
    """
    visited[start] = connected_component   # Помічаємо стартовий елемент як відвіданий
                                           # та запам'ятовуємо його компоненку зв'язності
    # для всіх сусідів стартового елементу
    for neighbour in graph[start].neighbors():
        if neighbour not in visited:  # які ще не були відвідані
            __dfs_helper(graph, visited, neighbour, connected_component)  # запускаємо DFS


def findConnectedComponent(graph: Graph):
    """ Перевіряє чи є неорієнтований граф зв'язним

    :param graph: Граф
    :return: Кількість компонент зв’язності неорієнтованого графа
    """
    assert not graph.mIsOriented     # Перевіряємо, що граф є не орієнтованим

    visited = {}    # Словник відвіданих вершин, містить пари
                    # (вершина: номер_компоненти_зв'язності)

    connected_component = 0   # Кількість компонент зв'язності графа
    for v in graph.vertices():
        if v not in visited:          # Якщо якась з вершин була не відвідана під час обходу
            connected_component += 1  # то з'явилася нова копонента зв'язності графа
            __dfs_helper(graph, visited, v, connected_component)  # запускаємо DFS з невідвідної вершини

    print(visited)    # Для тестування програми, виведемо відвідані вершини
                      # разом з номерами знайдених компонент зв'язності, до яких вони належать

    return connected_component  # Кількість компонент зв’язності неорієнтованого графа

if __name__ == "__main__":
    g = Graph()  # Створюємо неорієнтований граф

    # Перша компонента зв'язності
    g.addEdge(1, 4)  # ребро (1, 4)
    g.addEdge(1, 7)  # ребро (1, 7)
    g.addEdge(4, 7)  # ребро (4, 7)

    # Друга компонента зв'язності
    g.addEdge(2, 3)  # ребро (2, 3)
    g.addEdge(2, 5)  # ребро (2, 5)
    g.addEdge(3, 5)  # ребро (3, 5)
    g.addEdge(3, 6)  # ребро (3, 6)
    g.addEdge(5, 6)  # ребро (5, 6)

    print("Кількість компонент зв'язності: ", findConnectedComponent(g))
