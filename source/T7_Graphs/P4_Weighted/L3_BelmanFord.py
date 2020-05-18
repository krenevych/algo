from source.T7_Graphs.P4_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P4_Weighted.L1_VertexForAlgorithms import INF
from source.utils.benchmark import benchmark


@benchmark
def BelmanFord(graph: GraphForAlgorithms, start, end):
    """ Реалізує класичний алгоритм Беллмана-Форда для графів, що немають циклів від'ємної ваги

    :param graph: Граф
    :param start: Стартова вершина
    :param end: Кінцева вершина
    :return: Кортеж, що містить список вершин - найкоротший шлях, що сполучає вершини start та end та його вагу
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму
    for vertex in graph:
        vertex.setDistance(INF)  # Відстань для кожної вершини від стартової ставиться як нескінченність
        vertex.setSource(None)   # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань від першої вершини до неї ж визначається як 0
    graph[start].setDistance(0)

    for i in range(len(graph) - 1):
        for vertex in graph:                           # Для всіх вершин графу
            for neighbor_key in vertex.neighbors():    # Для всіх сусідів (за ключами) поточної вершини
                neighbor = graph[neighbor_key]         # Беремо вершину-сусіда за індексом
                newDist = vertex.distance() + vertex.weight(neighbor_key)    # Обчислюємо потенційну відстань у вершині-сусіді
                if newDist < neighbor.distance():      # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbor.setDistance(newDist)      # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                    neighbor.setSource(vertex.key())   # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї

    return graph.constructWay(start, end)

