from source.T6_Trees.P2_BinaryTree.L4_SearchTree import SearchTree


class SearchTreeWithDelete(SearchTree):
    """ Розширення класу бінарного дерева можливістю видаляти елементи """

    def delete(self, key):
        """ Видаляє заданий елемент у бінарному дереві

        :param key: Елемент, який потрібно видалити з бінарного дерева
        """
        self._delete_helper(self, key)

    def _search_max(self, root: SearchTree) -> SearchTree:
        """ Допоміжний рекурсивний метод пошуку найбільшого вузла у заданому піддереві.

            Згідно з властивостями бінарного дерева пошука, максимальний елемент може бути
            знайдений при проходженні дерева в глиб рухаючись лише по правих нащадках
        :param root: корінь піддерева у якому небхідно знайти найбільший вузол
        :return: знайдений вузол.
        """

        return self._search_max(root.mRightChild) if root.hasRight() else root

    def _delete_helper(self, root: SearchTree, key):
        """ Допоміжний рекурсиввий метод, що видаляє заданий елемент з дерева у заданому піддереві
            якщо такий елемент міситься у деремі. Пошук розпочинається з піддерева,
        що має коренем вершину startNode. Для технічних цілей передаємо у підпрограму
        предка вузла startNode - parent

        :param root: корінь піддерева у якому потрібно видалити заданий елемент
        :param key: Елемент, який потрібно видалити
        """

        node = self._search_helper(root, key)  # Знаходимо вузол, який треба видалити

        if node is None:  # Якщо шуканий елемент не міститься у дереві, то припиняємо роботу підпрограми
            return

        if node.hasNoChildren():      # Якщо знайдений вузол - листок (немає нащадків)
            if node.mParent is None:  # Якщо предок - корінь всього дерева
                node.mKey = None      # Робимо дерево порожнім
            else:
                if node.mParent.mLeftChild == node:
                    node.mParent.mLeftChild = None  # Видаляєм знайдений елемент
                else:
                    node.mParent.mRightChild = None  # Видаляєм знайдений елемент

        elif node.hasRight() and not node.hasLeft():  # Якщо знайдений вузол має лише одну праву гілку
            node.setNode(node.mRightChild)            # Замінюємо знайдений вузол його правим піддіревом

        elif node.hasLeft() and not node.hasRight():  # Якщо знайдений вузол має лише одну ліву гілку
            node.setNode(node.mLeftChild)             # Замінюємо знайдений вузол його лівим піддіревом

        else:                                             # Якщо знайдений вузол має обидві гілки
            left_max = self._search_max(node.mLeftChild)  # Знаходимо максимальний вузол у лівому піддереві
            left_max_key = left_max.mKey
            node.setNode(left_max_key)                    # Замінюємо значення елемета node знайденим максимальним
            self._delete_helper(node.mLeftChild, left_max_key)  # Видалення з лівого піддерева, найбільшого елементу


if __name__ == "__main__":
    t = SearchTreeWithDelete()
    t.addItems(12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16, 16)
    t.delete(9)
    t.delete(10)
    t.delete(8)

    print()
