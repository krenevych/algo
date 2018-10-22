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
        self.mItem = item            # навантаження кореня дерева
        self.mLeftChild  = None      # створюємо поле для лівого нащадка
        self.mRightChild = None      # створюємо поле для правого нащадка

        if left is not None:
            self.setLeft(left)    # встановлюємо лівий нащадок
        if right is not None:
            self.setRight(right)  # встановлюємо правий нащадок

    def empty(self):
        """ Перевіряє чи дерево порожнє, тобто чи має воно навантаження та нащадків

        :return: True, якщо дерево немає навантаження та нащадків
        """
        return (self.mItem is None
                and self.mLeftChild is None
                and self.mRightChild is None)

    def item(self):
        """ Повертає навантаження поточного вузла дерева

        :return: Навантаження
        """
        if self.empty():
            raise Exception('root: Дерево порожнє')
        return self.mItem

    def leftItem(self):
        """ Повертає навантаження лівого нащадка

        :return: Навантаження лівого нащадка
        """
        if self.hasLeft():
            return self.mLeftChild.item()

    def rightItem(self):
        """ Повертає навантаження правого нащадка

        :return: Навантаження правого нащадка
        """
        if self.hasRight():
            return self.mRightChild.item()

    def hasLeft(self):
        """ Чи містить дерево лівого нащадка

        :return: True, якщо дерево має лівого нащадка.
        """
        return self.mLeftChild is not None

    def hasRight(self):
        """ Чи містить дерево правого нащадка

        :return: True, якщо дерево має правого нащадка.
        """
        return self.mRightChild is not None

    def hasNoChildren(self):
        """ Визначає чи має дерево нащадків

        :return: True, якщо дерево немає нащадків.
        """
        return self.mLeftChild is None and self.mRightChild is None

    def leftChild(self):
        """ Повертає ліве піддерево поточного вузла

        :return: Ліве піддерево поточного вузла
        """
        return self.mLeftChild

    def rightChild(self):
        """Отримати праве піддерево."""
        return self.mRightChild

    def setNode(self, item):
        """ Змінює поточний вузол

        :param item: Нове піддерево або значення навантаження
        :return: None
        """
        if isinstance(item, BinaryTree):             # якщо item є деревом
            self.mItem = item.item()                 # змінюємо дані
            self.mLeftChild = item.leftChild()    # змінюємо ліве піддерево
            self.mRightChild = item.rightChild()  # змінюємо праве піддерево
        else:
            self.mItem = item

    def setLeft(self, item):
        """ Змінює лівого нащадка.

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, BinaryTree):         # якщо item є деревом
            self.mLeftChild = item               # змінюємо все піддерево
        elif self.hasLeft():                    # якщо дерево містить лівого нащадка
            self.mLeftChild.setNode(item)       # замінюємо вузол
        else:                                    # якщо дерево немає лівого нащадка
            self.mLeftChild = BinaryTree(item)   # створюємо дерево з вузлом item та робимо його лівим нащадком

    def setRight(self, item):
        """ Змінює правого нащадка

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, BinaryTree):         # якщо item є деревом
            self.mRightChild = item              # змінюємо все піддерево
        elif self.hasRight():                   # якщо дерево містить правого нащадка
            self.mRightChild.setNode(item)      # замінюємо вузол
        else:                                    # якщо дерево немає правого нащадка
            self.mRightChild = BinaryTree(item)  # створюємо дерево з вузлом item та робимо його правим нащадком

    def removeLeft(self):
        """ Видаляє лівого нащадка

        :return: None
        """
        self.mLeftChild = None

    def removeRight(self):
        """ Видаляє лівого нащадка

        :return: None
        """
        self.mRightChild = None

    def __str__(self):
        """ Зображення дерева у виляді рядка

        :return: Зображення дерева у виляді рядка
        """
        S = "               "
        if self.hasLeft():
            S += str(self.leftItem())

        S += " <- " + str(self.item()) + " -> "

        if self.hasRight():
            S += str(self.rightItem())
        return S


if __name__ == "__main__":

    B1 = BinaryTree(1, 11, 111)
    B3 = BinaryTree(3, 33, 333)
    B2 = BinaryTree(2, 22, B3)
    B = BinaryTree(item=0, left=B1, right=B2)

    print(B1.leftChild())
    print(B2)
    print(B3)
    print(B)
