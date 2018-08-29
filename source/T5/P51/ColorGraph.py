from source.T5.P51.Graph import Graph
from source.T5.P51.Vertex import Vertex

WHITE = 0  # Вершина білого кольору - вершина ще не відвідана
GRAY = 1   # Вершина сірого кольору - під час DFS ввійшли у вершину
BLACK = 2  # Вершина чорного кольору - під час DFS вийшли з вершини

class ColorVertex(Vertex):
    """ Допоміжний клас, (нащадок класу Vertex)

        має поле mColor - колір вершини, що
        використовується для алгортму топологічного сортування
    """
    def __init__(self, key):
        super().__init__(key)
        self.mColor = WHITE

    def set_color(self, color):
        self.mColor = color

    def color(self):
        return self.mColor


class ColorGraph(Graph):
    """ Граф, що містить вершини ColorVertex"""

    def add_vertex(self, vertex):
        """ Додає вершину у граф, якщо така вершина не міститься у ньому

        :param vertex: ключ (тобто ім'я) нової вершини
        :return: True, якщо вершина успішно додана
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = ColorVertex(vertex)     # створюємо нову вершину з іменем Vertex
        self.mVertices[vertex] = new_vertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1              # Збільшуємо лічильник вершин у графі
        return True
