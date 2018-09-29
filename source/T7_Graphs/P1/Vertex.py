from source.T7_Graphs.P1.VertexBase import VertexBase


class Vertex(VertexBase):

    def __init__(self, key):
        """ Конструктор створення вершини

        :param key: Ключ вершини
        """
        super().__init__(key)  # Викликаємо конструктор батьківського класу
        self.mNeighbors = {}   # Список сусідів вершини у вигляді пар (ім'я_сусіда: вага_ребра)

    def add_neighbor(self, vertex, weight=1):
        """ Додати сусіда

        Додає ребро, що сполучає поточну вершину з вершиною Vertex з вагою weight
        Vertex може бути або іншою вершиною, тобто об'єктом класу Vertex
        або ключем (ідентифікатором вершини)
        :param vertex: Вершина-сусід або ключ вершини
        :param weight: Вага ребра
        :return: None
        """
        if isinstance(vertex, VertexBase):  # Якщо Vertex - вершина
            self.mNeighbors[vertex.key()] = weight
        else:                            # Якщо Vertex - ім'я (ключ) вершини
            self.mNeighbors[vertex] = weight

    def neighbors(self):
        """ Повертає список ключів всіх сусідів поточної вершини

        :return: Список ключів всіх сусідів вершини
        """
        return self.mNeighbors.keys()

    def weight(self, neighbor):
        """ Повертає вагу ребра, що сполучає поточну вершину та вершину-сусіда

        :param neighbor: Вершина-сусід
        :return: Вага ребра
        """
        if isinstance(neighbor, VertexBase):  # Якщо aNeighbor - вершина (не ім'я)
            return self.mNeighbors[neighbor.key()]
        else:  # Якщо aNeighbor - ім'я (ключ) сусідньої вершини
            return self.mNeighbors[neighbor]

    def __str__(self):
        """ Зображення вершини у вигляді рядка у разом з усіма її сусідами """
        return super().__str__() + ' connected to: ' + str(self.mNeighbors)


if __name__ == "__main__":

    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)

    v1.add_neighbor(v1, 11)
    v1.add_neighbor(v2, 22)
    v1.add_neighbor(v3, 33)

    print(v1)
    print(v2)
    print(v3)

    print(v1.weight(v2))

