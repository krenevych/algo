class VertexBase:
    """ Базовий клас Vertex - вершина.

        Є базовим класом для класу, що описує вершину графа
        Клас містить поля - ключ (ім'я) вершини mId,
        а також її навантаження (тобто дані) mData.
    """

    def __init__(self, key):
        self.mKey = key  # Ключ (ім'я) вершини
        self.mData = None  # Навантаження (дані) вершини

    def key(self):
        """ Повертає ідентифікатор вершини """
        return self.mKey

    def set_data(self, data):
        """ Встановлює навантаження на вершину """
        self.mData = data

    def data(self):
        """ Повертає навантаження вершини """
        return self.mData

    def __str__(self):
        """ Зображення вершини у вигляді рядка """
        return str(self.mKey) + ": Data=" + str(self.data())


class Vertex(VertexBase):

    def __init__(self, key):
        super().__init__(key)  # Викликаємо конструктор батьківського класу
        self.mNeighbors = {}  # Список сусідів вершини у вигляді пар (ім'я_сусіда: вага_ребра)

    def add_neighbor(self, vertex, weight=1):
        """ Додати сусіда

        Додає ребро, що сполучає поточну вершину з вершиною Vertex з вагою weight
        Vertex може бути або іншою вершиною, тобто об'єктом класу Vertex
        або ключем (ідентифікатором вершини)
        """
        if isinstance(vertex, VertexBase):  # Якщо Vertex - вершина
            self.mNeighbors[vertex.key()] = weight
        else:  # Якщо Vertex - ім'я (ключ) вершини
            self.mNeighbors[vertex] = weight

    def neighbors(self):
        """ Повернути список ключів всіх сусідів поточної вершини """
        return self.mNeighbors.keys()

    def weight(self, neighbor):
        """Отримати вагу ребра, що сполучає поточну вершину та вершину-сусіда neighbor"""
        if isinstance(neighbor, VertexBase):  # Якщо aNeighbor - вершина (не ім'я)
            return self.mNeighbors[neighbor.key()]
        else:  # Якщо aNeighbor - ім'я (ключ) сусідньої вершини
            return self.mNeighbors[neighbor]

    def __str__(self):
        "Зображення вершини у вигляді рядка у разом з усіма її сусідами"
        return super().__str__() + ' connected to: ' + str(self.mNeighbors)


class Graph:
    """ Граф, що задається списком суміжних вершин """

    def __init__(self, oriented=False):
        self.mIsOriented = oriented  # Поле чи орієнтований граф
        self.mVertexNumber = 0  # Лічильник вершин у графі
        self.mVertices = {}  # Список (словник) вершин у графі у вигляді пар (ключ: вершина)

    def add_vertex(self, vertex):
        """ Додає вершину у граф, якщо така вершина не міститься у ньому

        Vertex - ключ (тобто ім'я) нової вершини
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = Vertex(vertex)  # створюємо нову вершину з іменем Vertex
        self.mVertices[vertex] = new_vertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1  # Збільшуємо лічильник вершин у графі
        return True

    def get_vertex(self, vertex):
        """ Повертає вершину графу, якщо така вершина міститься у графі """
        assert vertex in self

        # Визначаємо ключ вершини
        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.mVertices[key]

    def vertices(self):
        """ Повертає список всіх вершин у графі"""
        return self.mVertices

    def add_edge(self, source, destination, weight=1):
        """ Додавання ребра з кінцями в точках source та destination з вагою weight"""
        if source not in self:  # Якщо вершина source ще не міститься у графі
            self.add_vertex(source)  # додаємо вершину source
        if destination not in self:  # Якщо вершина destination ще не міститься у графі
            self.add_vertex(destination)  # додаємо вершину destination

        # Встановлюємо зв'язок (тобто ребро) між вершинами source та destination
        self[source].add_neighbor(destination, weight)

        if not self.mIsOriented:  # Якщо граф не орієнтований, то треба додати зворотній зв'язок
            self.mVertices[destination].add_neighbor(source, weight)

    def set_data(self, vertex, data):
        """ Встановлення навантаження data на вершину з іменем Vertex """
        assert vertex in self  # Перевірка чи міститься вершина в графі
        self[vertex].set_data(data)

    def get_data(self, vertex):
        """ Повернення навантаження вершини з іменем Vertex """
        assert vertex in self  # Перевірка чи міститься вершина в графі
        return self[vertex].data()

    def __contains__(self, vertex):
        """ Перевірка чи міститься вершина з іменем Vertex у графі """
        if isinstance(vertex, Vertex):  # Якщо Vertex - вершина (не ім'я)
            return vertex.key() in self.mVertices
        else:  # Якщо Vertex - ім'я (ключ) вершини
            return vertex in self.mVertices

    def __iter__(self):
        """ Ітератор для послідовного проходження всіх вершин у графі """
        return iter(self.mVertices.values())

    def __len__(self):
        """ Перевизначення методу len() як кількість вершин у графі """
        return self.mVertexNumber

    def __str__(self):
        """ Зображення графа разом з усіма вершинами і ребрами у вигляді рядка """
        s = ""
        for vertex in self:
            s = s + str(vertex) + "\n"
        return s

    def __getitem__(self, vertex):
        return self.get_vertex(vertex)


WHITE = 0  # Вершина білого кольору - вершина ще не відвідана
GRAY = 1  # Вершина сірого кольору - під час DFS ввійшли у вершину
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

        Vertex - ключ (тобто ім'я) нової вершини
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = ColorVertex(vertex)  # створюємо нову вершину з іменем Vertex
        self.mVertices[vertex] = new_vertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1  # Збільшуємо лічильник вершин у графі
        return True


def __helper(graph, vertex, sequence):
    """ Рекурсивний допоміжний метод """

    if vertex.color() == GRAY:  # Істиність цієї умови означає, що знайдено цикл,
        return True  # подальша робота алгоритму не має сенсу

    if vertex.color() == BLACK:  # вершина повністю опрацьована
        return False

    vertex.set_color(GRAY)  # помічаємо вершину сірим кольором, тобто ввійшли в неї
    for neighbour_key in graph[vertex].neighbors():  # для всіх сусідів стартового елементу
        neighbour = graph[neighbour_key]
        if __helper(graph, neighbour, sequence):
            return True

    vertex.set_color(BLACK)  # Помічаємо вершину як опрацьовану (чорним кольором)
    # sequence.insert(0, vertex.key())  # Вставляємо вершину у список топологічно відсортованих вершин
    sequence.append(vertex.key())  # Вставляємо вершину у список топологічно відсортованих вершин


def topological_sorting(graph):
    sequence = []  # Порожній список, що буде містити відсортовані елементи

    for vertex in graph:  # для всіх вершин графа запускаємо пошук в глибину
        cycle = __helper(graph, vertex, sequence)
        if cycle:
            return None

    return sequence  # Повертаємо список, що містить відсортовані елементи


gr = ColorGraph(True)  # Створюємо орієнтований граф

n, m = map(int, input().split())
for i in range(m):
    v1, v2 = map(int, input().split())
    gr.add_edge(v1, v2)

s = topological_sorting(gr)

if s is None:
    print(-1)
else:
    s.reverse()
    print(*s)


