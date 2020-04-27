from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.T7_Graphs.P1_Definitions.L5_Graph import Graph
from source.T7_Graphs.P4_Weighted.L1_VertexForAlgorithms import VertexForAlgorithms, INF


class GraphForAlgorithms(Graph):
    """Клас, що є розширенням класу для графа Graph
     Використовується у алгоритмах Дейкстри, Белмана-Форда...
     Міститть додаткову технічну інформацію, що необхідна для цих алгоритмів """

    def addVertex(self, vertex) -> bool:
        """ Додає вершину у граф, якщо така вершина не міститься у ньому

        :param vertex: ключ (тобто ім'я) нової вершини
        :return: True, якщо вершина успішно додана
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = VertexForAlgorithms(vertex)  # створюємо нову вершину з іменем key
        self.mVertices[vertex] = new_vertex       # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1                   # Збільшуємо лічильник вершин у графі
        return True

    def constructWay(self, start, end):
        """ Домопіжний метод, що будує шлях, між двома вершинами у графі
        Може бути застосовами лише після дії алгоритмів пошуку шляху
        (Хвильового, Дейкстри, Беллмана-Форда, тощо) які записують
        допоміжну інформацію у вершини графа.

        :param start: Вершина, що початком шляху
        :param end: Вершина, що є кінцем шляху
        :return: Кортеж, що містить список вершин - найкоротший шлях, що сполучає вершини start та end та його вагу
        """

        if self[end].source is None:  # шляху не існує
            return None, INF

        # будуємо шлях за допомогою стеку
        stack = Stack()
        current = end
        while True:
            stack.push(current)
            if current == start:
                break
            current = self[current].source()
            if current is None:
                return None

        way = []  # Послідовність вершин шляху
        while not stack.empty():
            way.append(stack.pop())

        # Повертаємо шлях та його вагу
        return way, self[end].distance()

