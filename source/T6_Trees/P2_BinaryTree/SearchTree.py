from source.T6_Trees.P2_BinaryTree.BinaryTree import BinaryTree


class SearchTree(BinaryTree):
    """ Клас - Бінарне дерево пошуку.

     Реалізує структуру даних, у якій вставка та пошук елементів здійснюється
     (в середньому) за логарифмічний час. """

    def insert(self, item):
        """ Метод, що реалізує вставку елемента у бінарне дерево

        :param item: елемент для вставки
        :return: None
        """
        #  запускаємо вставку item у дерево, починаючи з кореня
        self.__insert_helper(self, item)

    def search(self, item):
        """ Метод, що реалізує пошук елемента item у бінарному дереві

        :param item: Шуканий елемент
        :return: True, якщо елемент міститься у дереві та False - якщо елемент не знайдений.
        """
        #  запускаємо пошук item у дереві, починаючи з кореня
        return self.__search_helper(self, item)

    def add_items(self, *items):
        """ Додає послідовність елементів у дерево пошуку

        :param items: Послідовність елементів, що додаються у дерево пошуку
        :return: None
        """
        for item in items:
            self.insert(item)

    def __insert_helper(self, sub_tree, item):
        """ Допоміжний рекурсиввий метод, для вставки заданого елемента у задане піддерево.

        :param sub_tree: Піддерево у яке відбувається вставка нового елементу
        :param item: Елемент для вставки
        :return: None
        """

        if sub_tree.empty():                 # якщо піддерево з коренем startNode порожнє
            sub_tree.set_node(item)          # вставляємо елемент item
        else:
            node = sub_tree.node()           # беремо node - навантаження піддерева startNode

            if item < node:                  # якщо елемент для вставки має міститися у лівому піддереві
                if sub_tree.has_left():      # якщо дерево має лівого нащадка
                    #  запускаємо рекурсивно вставку item у ліве піддерево
                    self.__insert_helper(sub_tree.left_subtree(), item)
                else:                        # якщо дерево не має лівого нащадка
                    sub_tree.set_left(item)  # додаємо item у ролі лівого нащадка

            elif item > node:                # якщо елемент для вставки має міститися у правому піддереві
                if sub_tree.has_right():     # якщо дерево має правого нащадка
                    #  запускаємо рекурсивно вставку item у праве піддерево
                    self.__insert_helper(sub_tree.right_subtree(), item)
                else:                        # якщо дерево не має правого нащадка
                    sub_tree.set_right(item) # додаємо item у ролі правого нащадка

    def __search_helper(self, sub_tree, item):
        """ Допопоміжний рекурсиввий метод, для пошуку елементу у заданому піддереві.

        Пошук здійснюється проходом в глибину.
        :param sub_tree: Піддерево у якому здійснюється пошук
        :param item: Шуканий елемент
        :return: True, якщо елемент міститься у дереві та False - якщо елемент не знайдений.
        """
        if sub_tree.empty():             # якщо піддерево sub_tree порожнє, а отже
            return False                 # елемент item не знайдено повертаємо False
        else:
            node = sub_tree.node()       # node - навантаження піддерева sub_tree
            if node == item:             # якщо node є шуканим елементом,
                return True              # повертаємо True
            elif item < node:            # випадок: шуканий елемент може міститися у лівому піддереві
                if sub_tree.has_left():  # якщо дерево має лівого нащадка
                    #  запускаємо рекурсивний пошук item у лівому піддереві
                    return self.__search_helper(sub_tree.left_subtree(), item)
                else:                    # якщо дерево не має лівого нащадка
                    return False         # дерево не містить шуканого елемента item
            else:                        # випадок: шуканий елемент може міститися у правому піддереві
                if sub_tree.has_right(): # якщо дерево має правого нащадка
                    #  запускаємо рекурсивний пошук item у правому піддереві
                    return self.__search_helper(sub_tree.right_subtree(), item)
                else:                    # якщо дерево не має правого нащадка
                    return False         # дерево не містить шуканого елемента item


if __name__ == "__main__":
    t = SearchTree()
    t.add_items(10, 15, 3, 12, 122, 14, 133, 13, 1, 4, 90, 11)

    print(t)

    print(t.search(133))
    print(t.search(135))
    print(t.search(13))
    print(t.search(1))

    print()


