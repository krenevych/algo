class Node:
    """
    Клас, що реалізує вузол дерева
    """

    def __init__(self, key=None):
        """
        Конструктор - створює вузол дерева
        :param key: ключ вузла, що створюється
        """
        self.mKey = key

    def empty(self):
        """
        Перевіряє чи вузол порожній
        :return: True, якщо вузол порожній
        """
        return self.mKey is None

    def setKey(self, key):
        """
        Встановлює ключ для вузла
        :param key: нове значення ключа
        """
        self.mKey = key

    def key(self):
        """
        Повертає ключ вузла
        :return: ключ вузла
        """
        return self.mKey

    def __str__(self):
        """
        Повертає ключ вузла.
        :return: рядок, у вигляді "key"
        """
        return str(self.mKey)


