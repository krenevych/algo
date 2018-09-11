from source.T7_Graphs.P51.GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P51.VertexForAlgorithms import INF
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
        vertex.set_distance(INF)  # Відстань для кожної вершини від стартової ставиться як нескінченність
        vertex.set_source(None)   # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань від першої вершини до неї ж визначається як 0
    graph[start].set_distance(0)

    for i in range(len(graph) - 1):
        for vertex in graph:                         # Для всіх вершин графу
            for neighbor_key in vertex.neighbors():  # Для всіх сусідів (за ключами) поточної вершини
                neighbor = graph[neighbor_key]       # Беремо вершину-сусіда за індексом
                newDist = vertex.distance() + vertex.weight(neighbor_key)    # Обчислюємо потенційну відстань у вершині-сусіді
                if newDist < neighbor.distance():              # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbor.set_distance(newDist)       # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                    neighbor.set_source(vertex.key())   # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї

    return graph.construct_way(start, end)


def BelmanFordClasical(graph, start):
    """ Класичний алгоритм Беллмана-Форда для графів, що можуть мати цикли від'ємної ваги
        Перевіряє чи має граф цикли від'ємної ваги

    :param graph: Граф
    :param start: Стартова вершина
    :return: False, якщо граф не містить циклів від'ємної ваги
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму
    for vertex in graph:
        vertex.set_distance(INF)  # Відстань для кожної вершини від стартової ставиться як нескінченність
        vertex.set_source(None)   # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань від першої вершини до неї ж визначається як 0
    graph[start].set_distance(0)
    for i in range(len(graph) - 1):
        for vertex in graph:                             # Для всіх вершин графу
            for neighbor_key in vertex.neighbors():      # Для всіх сусідів (за ключами) поточної вершини
                neighbour = graph[neighbor_key]          # Беремо вершину-сусіда за індексом
                newDist = vertex.distance() + vertex.weight(neighbor_key)  # Обчислюємо потенційну відстань у вершині-сусіді
                if newDist < neighbour.distance():       # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbour.set_distance(newDist)      # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                    neighbour.set_source(vertex.key())   # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї

    # Перевірка на наявність циклів з від'ємною вагою
    # Тут фактично здійсюється ще одна ітерація циклу і якщо у одній з вершин знайдена відстань зменшиться,
    # то це і означатиме, що знайдено цикл від'ємної ваги.
    for vertex in graph:                            # Для всіх вершин графу
        for neighbor_key in vertex.neighbors():     # Для всіх сусідів (за ключами) поточної вершини
            neighbour = graph[neighbor_key]         # Беремо вершину-сусіда за індексом
            newDist = vertex.distance() + vertex.weight(neighbor_key)  # Обчислюємо потенційну відстань у вершині-сусіді
            if newDist < neighbour.distance():       # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                return True                          # Знайдено цикл від'ємної ваги.

    return False

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
        vertex.set_distance(INF)  # Відстань для кожної вершини від стартової ставиться як нескінченність
        vertex.set_source(None)   # Вершина з якої прийшли по найкорошому шляху невизначена

    # Відстань від першої вершини до неї ж визначається як 0
    graph[start].set_distance(0)

    for i in range(len(graph) - 1):
        isRelaxed = True        # Мітка, що алгоритм ще не закінчив роботу і необхідна принаймні ще одна його ітерація
        for vertex in graph:                            # Для всіх вершин графу
            for neighbor_key in vertex.neighbors():     # Для всіх сусідів (за ключами) поточної вершини
                neighbour = graph[neighbor_key]         # Беремо вершину-сусіда за ключем
                newDist = vertex.distance() + vertex.weight(neighbor_key)    # Обчислюємо потенційну відстань у вершині-сусіді
                if newDist < neighbour.distance():      # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbour.set_distance(newDist)     # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                    neighbour.set_source(vertex.key())  # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї
                    isRelaxed = False                   # Встановлюємо ознаку, що алгоритм потребує ще принаймні одного проходу

        if isRelaxed:  # Якщо на поточному кроці роботи алгоритму у знайдених раніше дістанціях у графі не відбулося жодних змін
            break      # припиняємо ітерації алгоритму, оскільки всі відстані знайдено

    return graph.construct_way(start, end)
