class VertexBase:
    """ Базовий клас Vertex - вершина.

        Є базовим класом для класу, що описує вершину графа
        Клас містить поля - ключ (ім'я) вершини mKey,
        а також її навантаження (тобто дані) mData.
    """

    def __init__(self, key):
        """ Конструктор створення вершини

        :param key: Ключ вершини
        """
        self.mKey = key    # Ключ (ім'я) вершини
        self.mData = None  # Навантаження (дані) вершини

    def key(self):
        """ Повертає ключ (ім'я) вершини

        :return: Ключ вершини
        """
        return self.mKey

    def setData(self, data):
        """ Встановлює навантаження на вершину

        :param data: Навантаження
        :return: None
        """
        self.mData = data

    def data(self):
        """ Повертає навантаження вершини

        :return: Навантаження вершини
        """
        return self.mData

    def __str__(self):
        """ Зображення вершини у вигляді рядка """
        return str(self.mKey) + ": Data=" + str(self.data())