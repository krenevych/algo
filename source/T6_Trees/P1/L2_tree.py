class Tree:
    """
    Клас, що реалізує структуру даних дерево
    """

    def __init__(self, key=None):
        """
        Конструктор - створює вузол дерева
        :param key: ключ вузла, що створюється
        """
        self.key = key
        self.children = []

    def empty(self):
        """
        Перевіряє чи дерево порожнє
        :return: True, якщо дерево порожнє
        """
        return self.key is None and len(self.children) == 0

    def setKey(self, key):
        """
        Встановлює ключ для поточного вузла
        :param key: нове значення ключа
        """
        self.key = key

    def addChild(self, child):
        """
        Додає до поточного вузла заданий вузол (разом з відповідним піддеревом)
        :param child: вузол (піддерево), що додається
        """
        self.children.append(child)

    def removeChild(self, key):
        """
         Видаляє у поточному вузлі вузол-дитину
        :param key: ключ вузла, що видаляється
        :return: False, якщо вузол не містить дитину заданим ключем
        """
        for child in self.children:
            if child.getKey() == key:
                self.children.remove(child)
                return True
        return False

    def getKey(self):
        """
        Повертає ключ поточного вузла
        :return: ключ поточного вузла
        """
        return self.key

    def getChildren(self):
        """
        Повертає список дітей поточного вузла
        :return: Список дітей
        """
        return self.children

    def getChild(self, key):
        """
        За заданим ключем, повертає вузол зі списку дітей
        :param key: ключ вузла
        :return: знайдений вузол якщо його знайдено, None у іншому випадку
        """
        for child in self.children:
            if child.getKey() == key:
                return child
        return None  # якщо ключ не знайдено

    def __str__(self):
        """
        Повертає ключ вузла і список ключів дітей.
        :return: рядок, у вигляді "key1 : [child1, child2, child13,...]"
        """
        return str(self.key) + " : " + str([el.getKey() for el in self.children])


def createSampleTree():
    """
    Створювати дерево будемо знизу вгору - спочатку листя,
    потім внутрішні вузли, додаючи до них відповідні піддерева.
    Корінь створимо останнім і додамо до нього відповідні піддерева.
    """

    # Створимо вузли, що є листям дерева
    node7 = Tree(7)
    node9 = Tree(9)
    node10 = Tree(10)
    node11 = Tree(11)
    node12 = Tree(12)
    node13 = Tree(13)
    node14 = Tree(14)
    node15 = Tree(15)

    # Створимо внутрішні вузли дерева та додаємо до них піддерева
    node8 = Tree(8)
    node8.addChild(node14)
    node8.addChild(node15)

    node4 = Tree(4)
    node4.addChild(node8)
    node4.addChild(node9)

    node5 = Tree(5)
    node5.addChild(node10)
    node5.addChild(node11)

    node2 = Tree(2)
    node2.addChild(node4)
    node2.addChild(node5)

    node6 = Tree(6)
    node6.addChild(node12)
    node6.addChild(node13)

    node3 = Tree(3)
    node3.addChild(node6)
    node3.addChild(node7)

    # Створюємо корінь дерева та додаємо до нього відповідні вузли
    root = Tree(1)
    root.addChild(node2)
    root.addChild(node3)

    return root



# Головна програма – виклик підпрограми, що створює дерево
if __name__ == "__main__":
    tree = createSampleTree()

    node11 = tree.getChild(2).getChild(5).getChild(11)

    print(node11)

