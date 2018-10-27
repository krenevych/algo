class BinaryTree:
    """ Реалізує бінарне дерево.

    Дерево реалізується рекурсивним чином. Фактично кожен вузол дерева є деревом,
    що місить навантаження та посилання на двох дітей
    - лівого та правого - які у свою чергу також є деревами (вузлами дерева)
    Надалі тут будемо ототожнювати вузол дерева з його навантаженням, а лівого та правого
    синів будемо називати лівим та правим піддеревом відповідно.

    """

    def __init__(self, item=None, left=None, right=None):
        """ Конструктор

        Створює новий вузол дерева - корінь та ініціалізує його заданими даними

        :param item: Навантаження вузла
        :param left: ліве піддерево
        :param right: праве піддерево
        """
        self.mItem = item            # навантаження кореня дерева
        self.mLeftChild  = None      # створюємо поле для лівого сина
        self.mRightChild = None      # створюємо поле для правого сина

        if left is not None:
            self.setLeft(left)    # встановлюємо лівого сина
        if right is not None:
            self.setRight(right)  # встановлюємо правого сина

    def empty(self):
        """ Перевіряє чи дерево порожнє, тобто чи має воно навантаження та дітей

        :return: True, якщо дерево немає навантаження та дітей
        """
        return (self.mItem is None
                and self.mLeftChild is None
                and self.mRightChild is None)

    def item(self):
        """ Повертає навантаження поточного вузла дерева

        :return: Навантаження
        """
        if self.empty():
            raise Exception('BinaryTree: Дерево порожнє')
        return self.mItem

    def leftItem(self):
        """ Повертає навантаження лівого сина

        :return: Навантаження лівого сина
        """
        if self.hasLeft():
            return self.mLeftChild.item()

    def rightItem(self):
        """ Повертає навантаження правого сина

        :return: Навантаження правого сина
        """
        if self.hasRight():
            return self.mRightChild.item()

    def hasLeft(self):
        """ Чи містить дерево лівого сина

        :return: True, якщо дерево має лівого сина.
        """
        return self.mLeftChild is not None

    def hasRight(self):
        """ Чи містить дерево правого сина

        :return: True, якщо дерево має правого сина.
        """
        return self.mRightChild is not None

    def hasNoChildren(self):
        """ Визначає чи має дерево дітей

        :return: True, якщо дерево немає дітей.
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
        if isinstance(item, BinaryTree):          # якщо item є деревом
            self.mItem = item.item()              # змінюємо дані
            self.mLeftChild = item.leftChild()    # змінюємо ліве піддерево
            self.mRightChild = item.rightChild()  # змінюємо праве піддерево
        else:
            self.mItem = item

    def setLeft(self, item):
        """ Змінює лівого сина.

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, BinaryTree):        # якщо item є деревом
            self.mLeftChild = item              # змінюємо все піддерево
        elif self.hasLeft():                    # якщо дерево містить лівого сина
            self.mLeftChild.setNode(item)       # замінюємо вузол
        else:                                   # якщо дерево немає лівого сина
            self.mLeftChild = BinaryTree(item)  # створюємо дерево з вузлом item та робимо його лівим сином

    def setRight(self, item):
        """ Змінює правого сина

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, BinaryTree):         # якщо item є деревом
            self.mRightChild = item              # змінюємо все піддерево
        elif self.hasRight():                    # якщо дерево містить правого сина
            self.mRightChild.setNode(item)       # замінюємо вузол
        else:                                    # якщо дерево немає правого сина
            self.mRightChild = BinaryTree(item)  # створюємо дерево з вузлом item та робимо його правим сином

    def removeLeft(self):
        """ Видаляє лівого сина """
        self.mLeftChild = None

    def removeRight(self):
        """ Видаляє лівого сина """
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


def createSampleTree():
    """
    Приклад створення бінарного дерева
    """

    # Створимо внутрішні вузли дерева та додаємо до них піддерева
    node8 = BinaryTree(8) # Створення вузла з ключем 8
    node8.setLeft(14)     # Додавання лівого піддерева, додаючи листок 14
    node8.setRight(15)    # Додавання правого піддерева, додаючи листок 15

    node4 = BinaryTree(4) # Створення вузла з ключем 4
    node4.setLeft(node8)  # Додавання лівого піддерева
    node4.setRight(9)     # Додавання правого піддерева, додаючи листок 9

    node5 = BinaryTree(5) # Створення вузла з ключем 5
    node5.setLeft(10)    # Додавання лівого піддерева, додаючи листок 10
    node5.setRight(11)   # Додавання правого піддерева, додаючи листокм 11

    node2 = BinaryTree(2)  # Створення вузла з ключем 2
    node2.setLeft(node4)   # Додавання лівого піддерева, додаючи листок
    node2.setRight(node5)  # Додавання правого піддерева, додаючи піддерево

    node6 = BinaryTree(6)
    node6.setLeft(12)   # Додавання лівого піддерева, додаючи листок 12
    node6.setRight(13)  # Додавання правого піддерева, додаючи листок 13

    node3 = BinaryTree(3) # Створення вузла з ключем 3
    node3.setLeft(node6)  # Додавання лівого піддерева
    node3.setRight(7)     # Додавання правого піддерева, додаючи листок 7

    # Створюємо корінь дерева та додаємо до нього відповідні вузли
    root = BinaryTree(1)
    root.setLeft(node2)   # Додавання лівого піддерева до кореня
    root.setRight(node3)  # Додавання правого піддерева до кореня

    return root  # Функція повертає корінь створеного дерева


if __name__ == "__main__":

    B = createSampleTree()
    print(B)
