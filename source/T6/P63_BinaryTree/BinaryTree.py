class BinaryTree:
    """ Реалізує бінарне дерево.

    Дерево реалізується рекурсивним чином. Фактично кожен вузол дерева є деревом,
    що місить навантаження та посилання на двох нащадків
    - лівого та правого - які у свою чергу також є деревами (вузлами дерева)
    Надалі тут будемо ототожнювати вузло дерева з його навантаженням, а лівого та правого
    нащадків будемо називати лівим та правим піддеревом відповідно.

    """

    def __init__(self, item=None, left=None, right=None):
        """ Конструктор

        Створює новий вузол дерева - корінь та ініціалізує його заданими даними

        :param item: Навантаження вузла
        :param left: ліве піддерево
        :param right: праве піддерево
        """
        self.mNode = item                 # навантаження кореня дерева
        self.mLeftChild = None            # створюємо поле для лівого нащадка
        self.mRightChild = None           # створюємо поле для правого нащадка

        if left is not None:
            self.set_left(left)    # встановлюємо лівий нащадок
        if right is not None:
            self.set_right(right)  # встановлюємо правий нащадок

    def empty(self):
        """ Перевіряє чи дерево порожнє, тобто чи має воно навантаження та нащадків

        :return: True, якщо дерево немає навантаження та нащадків
        """
        return (self.mNode is None
                and self.mLeftChild is None
                and self.mRightChild is None)

    def node(self):
        """ Повертає навантаження поточного вузла дерева

        :return: Навантаження
        """
        if self.empty():
            raise Exception('root: Дерево порожнє')
        return self.mNode

    def left_node(self):
        """ Повертає навантаження лівого нащадка

        :return: Навантаження лівого нащадка
        """
        if self.has_left():
            return self.mLeftChild.node()

    def right_node(self):
        """ Повертає навантаження правого нащадка

        :return: Навантаження правого нащадка
        """
        if self.has_right():
            return self.mRightChild.node()

    def has_left(self):
        """ Чи містить дерево лівого нащадка

        :return: True, якщо дерево має лівого нащадка.
        """
        return self.mLeftChild is not None

    def has_right(self):
        """ Чи містить дерево правого нащадка

        :return: True, якщо дерево має правого нащадка.
        """
        return self.mRightChild is not None

    def has_no_children(self):
        """ Визначає чи має дерево нащадків

        :return: True, якщо дерево немає нащадків.
        """
        return self.mLeftChild is None and self.mRightChild is None

    def left_subtree(self):
        """ Повертає ліве піддерево поточного вузла

        :return: Ліве піддерево поточного вузла
        """
        return self.mLeftChild

    def right_subtree(self):
        """Отримати праве піддерево."""
        return self.mRightChild

    def set_node(self, item):
        """ Змінює поточний вузол

        :param item: Нове піддерево або значення навантаження
        :return: None
        """
        if isinstance(item, BinaryTree):             # якщо item є деревом
            self.mNode = item.node()                 # змінюємо дані
            self.mLeftChild = item.left_subtree()    # змінюємо ліве піддерево
            self.mRightChild = item.right_subtree()  # змінюємо праве піддерево
        else:
            self.mNode = item

    def set_left(self, item):
        """ Змінює лівого нащадка.

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, BinaryTree):         # якщо item є деревом
            self.mLeftChild = item               # змінюємо все піддерево
        elif self.has_left():                    # якщо дерево містить лівого нащадка
            self.mLeftChild.set_node(item)       # замінюємо вузол
        else:                                    # якщо дерево немає лівого нащадка
            self.mLeftChild = BinaryTree(item)   # створюємо дерево з вузлом item та робимо його лівим нащадком

    def set_right(self, item):
        """ Змінює правого нащадка

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, BinaryTree):         # якщо item є деревом
            self.mRightChild = item              # змінюємо все піддерево
        elif self.has_right():                   # якщо дерево містить правого нащадка
            self.mRightChild.set_node(item)      # замінюємо вузол
        else:                                    # якщо дерево немає правого нащадка
            self.mRightChild = BinaryTree(item)  # створюємо дерево з вузлом item та робимо його правим нащадком

    def remove_left(self):
        """ Видаляє лівого нащадка

        :return: None
        """
        self.mLeftChild = None

    def remove_right(self):
        """ Видаляє лівого нащадка

        :return: None
        """
        self.mRightChild = None

    def remove_child(self, item):
        """ Видаляє нащадка із заданим значенням навантаження

        :param item: Навантаження
        :return: None
        """
        if self.has_left() and self.left_node() == item:
            self.remove_left()
        elif self.has_right() and self.right_node() == item:
            self.remove_right()

    def __str__(self):
        """ Зображення дерева у виляді рядка

        :return: Зображення дерева у виляді рядка
        """
        S = "               "
        if self.has_left():
            S += str(self.left_node())

        S += " <- " + str(self.node()) + " -> "

        if self.has_right():
            S += str(self.right_node())
        return S


if __name__ == "__main__":

    B1 = BinaryTree(1, 11, 111)
    B3 = BinaryTree(3, 33, 333)
    B2 = BinaryTree(2, 22, B3)
    B = BinaryTree(item=0, left=B1, right=B2)

    print(B1.left_subtree())
    print(B2)
    print(B3)
    print(B)
