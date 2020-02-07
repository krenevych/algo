from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree


class SearchTree(BinaryTree):
    """ Клас - Бінарне дерево пошуку.

     Реалізує структуру даних, у якій вставка та пошук елементів здійснюється
     (в середньому) за логарифмічний час. """

    def search(self, key):
        """ Метод, що реалізує пошук елемента item у бінарному дереві
            Не рекурсивна реалізація

        :param key: Шуканий елемент
        :return: Вузол з ключем key якщо такий елемент міститься у дереві та None - якщо елемент не знайдений.
        """
        current_node = self   # починаємо з кореня
        while current_node is not None:
            if current_node.mKey == key:
                return current_node
            elif current_node.mKey > key:
                current_node = current_node.mLeftChild
            else:
                current_node = current_node.mRightChild

        return None

    def insert(self, key):
        """ Метод, що реалізує вставку елемента у бінарне дерево
            Не рекурсивна реалізація

        :param key: ключ, що необхідно вставити
        """
        if self.empty():                # якщо піддерево з коренем startNode порожнє
            self.setNode(key)           # вставляємо елемент item
        else:
            current_node = self         # починаємо з кореня
            while True:
                if current_node.mKey == key:
                    break
                elif current_node.mKey > key:
                    if current_node.hasLeft():
                        current_node = current_node.mLeftChild
                    else:
                        current_node.setLeft(key)
                        break
                elif current_node.mKey < key:
                    if current_node.hasRight():
                        current_node = current_node.mRightChild
                    else:
                        current_node.setRight(key)
                        break

    def addItems(self, *items):
        """ Додає послідовність елементів у дерево пошуку

        :param items: Послідовність елементів, що додаються у дерево пошуку
        :return: None
        """
        for item in items:
            self.insert(item)


if __name__ == "__main__":
    t = SearchTree()
    t.addItems(12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16, 16)

    print(t)

    print(t.search(10))
    print(t.search(5))
    print(t.search(21))
    print(t.search(111))

    print()


