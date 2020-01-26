class Node:
    """ Допоміжний клас - вузол списку. """

    def __init__(self, item):
        """ Конструктор

        :param item: навантаження вузла
        """
        self.mItem = item   # навантаження вузла
        self.mNext = None   # посилання на наступний вузол списку