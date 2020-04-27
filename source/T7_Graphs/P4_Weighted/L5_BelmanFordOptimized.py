from source.T7_Graphs.P4_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P4_Weighted.L1_VertexForAlgorithms import INF
from source.utils.benchmark import benchmark


@benchmark
def BelmanFordOptimized(graph: GraphForAlgorithms, start: int, end: int):
    """ Оптимізований алгоритм Беллмана-Форда для графів, що немають циклів від'ємної ваги
        Тут здійснюється перевірка, що якщо на певному кроці роботи алгоритму не відбулося
        жодних змін у дистанціях, в вершинах знайдених на попередньому кроці,
        то алгоритм фактично закінчив свою роботу

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
        isRelaxed = True        # Мітка, що алгоритм ще не закінчив роботу і необхідна принаймні ще одна його ітерація
        for vertex in graph:                            # Для всіх вершин графу
            for neighbor_key in vertex.neighbors():     # Для всіх сусідів (за ключами) поточної вершини
                neighbour = graph[neighbor_key]         # Беремо вершину-сусіда за ключем
                newDist = vertex.distance() + vertex.weight(neighbor_key)    # Обчислюємо потенційну відстань у вершині-сусіді
                if newDist < neighbour.distance():      # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbour.setDistance(newDist)     # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                    neighbour.setSource(vertex.key())  # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї
                    isRelaxed = False                   # Встановлюємо ознаку, що алгоритм потребує ще принаймні одного проходу

        if isRelaxed:  # Якщо на поточному кроці роботи алгоритму у знайдених раніше дістанціях у графі не відбулося жодних змін
            break      # припиняємо ітерації алгоритму, оскільки всі відстані знайдено

    return graph.constructWay(start, end)
