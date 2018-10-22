"""
Алгоритм Прима - алгоритм побудови мінімального кістякового дерева зваженого зв'язного неорієнтованого графа. Це жадібний алгоритм.

Побудова починається з дерева, що включає в себе одну (довільну) вершину. Протягом роботи алгоритму дерево розростається, поки не охопить
всі вершини вихідного графа. На кожному кроці алгоритму до поточного дереву приєднується найлегше з ребер, що з'єднують вершину з 
побудованого дерева і вершину, що не належить до дерева.

https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9F%D1%80%D0%B8%D0%BC%D0%B0

"""
from source.T7_Graphs.P1.GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P1.VertexForAlgorithms import INF
from source.T7_Graphs.P2.Connectivity import checkConnected
from source.T6_Trees.P2_BinaryTree.L7_PriorityQueue import PriorityQueue
from source.utils.benchmark import benchmark


@benchmark
def Prim(graph: GraphForAlgorithms):
    """ Реалізує алгоритм Пріма побудови каркасного дерева

    :param graph: заданий граф на базі якого будується каркасне дерево
    :return: граф, що є мінімальним каркасним деревом для заданого графа
    """

    assert not graph.mIsOriented
    assert checkConnected(graph)

    start = 0  # Вибираємо довільну точку графа як початкову з якої стартує алгоритм

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму.
    # У алгоритмі Прима, як і у алгоритмі Дейкстри ця додаткова інформація визначається у кожній вершині
    # як відстань від точки, до вже побудованого дерева вершини до неї.
    for vertex in graph:
        vertex.set_distance(INF)  # Відстань для кожної вершини ініціалізується як нескінченність
        vertex.set_source(None)   # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань у старотовій вершині (тобто від стартової вершини до себе) визначається як 0
    graph[start].set_distance(0)

    pq = PriorityQueue()  # Створюємо пріоритетну чергу

    # Додаємо у чергу з пріоритетом всі вершини графа.
    for vertex in graph:
        pq.insert(vertex.key(), vertex.distance())  # де пріоритет - це відстань у вершині

    while not pq.empty():

        vertex_key = pq.extractMinimum()  # Беремо індекс вершини з черги з найнижчим пріоритетом
        vertex = graph[vertex_key]         # Беремо вершину за індексом

        for neighbor_key in vertex.neighbors():        # Для всіх сусідів (за ключами) поточної вершини
            neighbour = graph[neighbor_key]            # Беремо вершину-сусіда за індексом
            newDist = vertex.weight(neighbor_key)      # Визначаємо вагу ребра між вершиною та вершиною-сусідом
            if neighbor_key in pq and newDist < neighbour.distance():   # Якщо вершина-сусід ще не додана до каркасного дерева і
                                                             # потенційна відстань у вершині-сусіді менша за її поточне значення
                neighbour.set_distance(newDist)              # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                neighbour.set_source(vertex_key)             # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї
                pq.decreasePriority(neighbor_key, newDist)  # перераховуємо її пріоритет в черзі

    # Будуємо граф, що є каркасним деревом
    spanning_tree = GraphForAlgorithms()
    for vertex in graph:
        destination = vertex.key()
        source = vertex.source()
        if source is None:
            continue
        weight = vertex.weight(source)
        spanning_tree.add_edge(source, destination, weight)

    return spanning_tree


def __treeWeightHelper(graph, visited, start):
    """ Допоміжний рекурсивний метод, який, використовуючи обхід в глибину,
    визначає вагу заданого каркасного дерева (суму ваг усіх ребер)

    :param graph: Заданий граф
    :param visited: Допоміжний список, i-й елемент якого містить позначку чи була відвідана i-та вершина
    :param start: Вершина з якої відбувається запуск обходу в глибину
    :return: Вагу графа
    """
    res = 0
    visited[start] = True  # Помічаємо стартовий елемент як відвіданий
    # для всіх сусідів стартового елементу
    for neighbour in graph[start].neighbors():
        if not visited[neighbour]:          # які ще не були відвідані
            res += graph[start].weight(neighbour)
            res += __treeWeightHelper(graph, visited, neighbour)

    return res

def treeWeight(graph):
    """ Функція знаходження ваги отриманого дерева

    :param graph: Заданий граф
    :return: Вагу графа
    """
    visited = [False] * len(graph)
    return __treeWeightHelper(graph, visited, 0)


if __name__ == "__main__":   # Для тестування

    g = GraphForAlgorithms()

    g.add_edge(0, 1, 7)
    g.add_edge(0, 5, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 4, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 0, 5)
    g.add_edge(5, 4, 2)
    g.add_edge(5, 2, 3)
    g.add_edge(6, 3, 1)
    g.add_edge(6, 2, 1)
    g.add_edge(6, 7, 12)
    g.add_edge(7, 4, 2)

    # t = GraphForAlgorithms()
    t = Prim(g)
    print(t)
    print(treeWeight(t))

