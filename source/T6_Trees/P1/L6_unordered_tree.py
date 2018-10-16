class UnorderedTree:
    """
    Клас, що реалізує структуру даних невпорядковане дерево
    """

    def __init__(self, key=None):
        """
        Конструктор - створює вузол дерева
        :param key: ключ вузла, що створюється
        """
        self.mKey = key       # ключ вузла
        self.mChildren = {}   # словник дітей вузла, місить пари {ключ: піддерево}

    def empty(self):
        """
        Перевіряє чи дерево порожнє
        :return: True, якщо дерево порожнє
        """
        return self.mKey is None and len(self.mChildren) == 0

    def setKey(self, key):
        """
        Встановлює ключ для поточного вузла
        :param key: нове значення ключа
        """
        self.mKey = key

    def addChild(self, child):
        """
        Додає до поточного вузла заданий вузол (разом з відповідним піддеревом)
        :param child: вузол (піддерево), що додається
        """
        self.mChildren[child.key()] = child

    def removeChild(self, key):
        """
         Видаляє у поточному вузлі вузол-дитину
        :param key: ключ вузла, що видаляється
        :return: False, якщо вузол не містить дитину заданим ключем
        """
        if key in self.mChildren:
            del self.mChildren[key]
            return True
        else:
            return False

    def key(self):
        """
        Повертає ключ поточного вузла
        :return: ключ поточного вузла
        """
        return self.mKey

    def getChildren(self):
        """
        Повертає словник дітей поточного вузла
        :return: Список дітей
        """
        return self.mChildren

    def getChild(self, key):
        """
        За заданим ключем, повертає вузол зі списку дітей
        :param key: ключ вузла
        :return: знайдений вузол якщо його знайдено, None у іншому випадку
        """
        if key in self.mChildren:
            return self.mChildren[key]
        else:
            return None

    def __str__(self):
        """
        Повертає ключ вузла і список ключів дітей.
        :return: рядок, у вигляді "key1 : [child1, child2, child13,...]"
        """
        return str(self.mKey) + " : " + str(self.mChildren.keys())


def createSampleTree():
    """
    Створювати дерево будемо знизу вгору - спочатку листя,
    потім внутрішні вузли, додаючи до них відповідні піддерева.
    Корінь створимо останнім і додамо до нього відповідні піддерева.
    """

    # Створимо вузли, що є листям дерева
    node7 = UnorderedTree(7)
    node9 = UnorderedTree(9)
    node10 = UnorderedTree(10)
    node11 = UnorderedTree(11)
    node12 = UnorderedTree(12)
    node13 = UnorderedTree(13)
    node14 = UnorderedTree(14)
    node15 = UnorderedTree(15)

    # Створимо внутрішні вузли дерева та додаємо до них піддерева
    node8 = UnorderedTree(8)
    node8.addChild(node14)
    node8.addChild(node15)

    node4 = UnorderedTree(4)
    node4.addChild(node8)
    node4.addChild(node9)

    node5 = UnorderedTree(5)
    node5.addChild(node10)
    node5.addChild(node11)

    node2 = UnorderedTree(2)
    node2.addChild(node4)
    node2.addChild(node5)

    node6 = UnorderedTree(6)
    node6.addChild(node12)
    node6.addChild(node13)

    node3 = UnorderedTree(3)
    node3.addChild(node6)
    node3.addChild(node7)

    # Створюємо корінь дерева та додаємо до нього відповідні вузли
    root = UnorderedTree(1)
    root.addChild(node2)
    root.addChild(node3)

    return root



# Головна програма – виклик підпрограми, що створює дерево
if __name__ == "__main__":
    tree = createSampleTree()

    node11 = tree.getChild(2).getChild(5).getChild(11)

    print(node11)

