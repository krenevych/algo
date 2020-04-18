from source.T6_Trees.P2_BinaryTree.L4_SearchTree import SearchTree


class SearchTreeWithDelete(SearchTree):
    """ Розширення класу бінарного дерева можливістю видаляти елементи """

    def delete(self, key):
        """ Видаляє заданий елемент у бінарному дереві

        :param key: Елемент, який потрібно видалити з бінарного дерева
        """
        self._delete_helper(self, key)

    @staticmethod
    def _delete_helper(root, key):
        """ Допоміжний рекурсиввий метод, що видаляє заданий елемент з дерева у заданому піддереві
            якщо такий елемент міситься у деремі. Пошук розпочинається з піддерева,
        що має коренем вершину startNode. Для технічних цілей передаємо у підпрограму
        предка вузла startNode - parent

        :param root: корінь піддерева у якому потрібно видалити заданий елемент
        :param key: Елемент, який потрібно видалити
        """

        node = SearchTreeWithDelete._search_helper(root, key)  # Знаходимо вузол, який треба видалити

        if node is None:  # Якщо шуканий елемент не міститься у дереві, то припиняємо роботу підпрограми
            return

        if node.hasNoChildren():      # Якщо знайдений вузол - листок (немає нащадків)
            node.removeSelfFromParent()

        elif node.hasLeft() and not node.hasRight():  # Якщо знайдений вузол має лише одну ліву гілку
            node.setNode(node.mLeftChild)             # Замінюємо знайдений вузол його лівим піддіревом

        elif node.hasRight() and not node.hasLeft():  # Якщо знайдений вузол має лише одну праву гілку
            node.setNode(node.mRightChild)            # Замінюємо знайдений вузол його правим піддеревом

        else:                                         # Якщо знайдений вузол має обидві гілки
            left_max = SearchTreeWithDelete._search_max(node.mLeftChild)  # Знаходимо максимальний вузол у лівому піддереві
            left_max_key = left_max.mKey
            node.setNode(left_max_key)                # Замінюємо значення елемета node знайденим максимальним
            SearchTreeWithDelete._delete_helper(node.mLeftChild, left_max_key)  # Видалення з лівого піддерева найбільшого елементу


