from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree


class SearchTree(BinaryTree):
    """ Клас - Бінарне дерево пошуку.

     Реалізує структуру даних, у якій вставка та пошук елементів здійснюється
     (в середньому) за логарифмічний час. """

    def search(self, key):
        """ Метод, що реалізує пошук елемента item у бінарному дереві

        :param key: Шуканий елемент
        :return: Вузол з ключем key якщо такий елемент міститься у дереві та None - якщо елемент не знайдений.
        """
        return self._search_helper(self, key)  # запускаємо пошук вузла з ключем key у дереві, починаючи з кореня

    def _search_helper(self, root, key):
        """ Допопоміжний рекурсиввий метод, для пошуку елементу у заданому піддереві.

        Пошук здійснюється проходом в глибину.
        :param root: корінь піддерева у якому здійснюється пошук
        :param key: Шуканий елемент
        :return: посилання на знайдений елемент, якщо елемент міститься у дереві та None - якщо елемент не знайдений.
        """
        if root.empty():             # якщо піддерево sub_tree порожнє,
            return None              # а отже вузол не знайдено - повертаємо None
        else:
            if root.mKey == key:     # якщо ключ поточного вузла збігається з шуканим,
                return root          # повертаємо знайдений вузол
            elif key < root.mKey:    # випадок: шуканий елемент може міститися у лівому піддереві
                return self._search_helper(root.mLeftChild, key) if root.hasLeft() else None
            else:                    # випадок: шуканий елемент може міститися у правому піддереві
                return self._search_helper(root.mRightChild, key) if root.hasRight() else None

    def insert(self, key):
        """ Метод, що реалізує вставку елемента у бінарне дерево

        :param key: ключ, що необхідно вставити
        """
        self._insert_helper(self, key)  # запускаємо вставку елемента key у дерево, починаючи з кореня

    def _insert_helper(self, root, key):
        """ Допоміжний рекурсиввий метод, для вставки заданого елемента у задане піддерево.

        :param root: корінь піддерева у яке відбувається вставка нового елементу
        :param key: Елемент для вставки
        """

        if root.empty():                # якщо піддерево з коренем startNode порожнє
            root.setNode(key)           # вставляємо елемент item
        else:

            if key < root.mKey:         # якщо елемент для вставки має міститися у лівому піддереві
                if root.hasLeft():      # якщо дерево має лівого нащадка
                    #  запускаємо рекурсивно вставку item у ліве піддерево
                    self._insert_helper(root.mLeftChild, key)
                else:                   # якщо дерево не має лівого нащадка
                    root.setLeft(key)   # додаємо item у ролі лівого нащадка

            elif key > root.mKey:        # якщо елемент для вставки має міститися у правому піддереві
                if root.hasRight():      # якщо дерево має правого нащадка
                    #  запускаємо рекурсивно вставку item у праве піддерево
                    self._insert_helper(root.mRightChild, key)
                else:                        # якщо дерево не має правого нащадка
                    root.setRight(key)  # додаємо item у ролі правого нащадка

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


