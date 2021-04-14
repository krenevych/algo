from source.T6_Trees.P2_BinaryTree.L7_AvlTree import AVLTree


class AVLTreeWithDelete(AVLTree):
    """ Розширення класу бінарного дерева можливістю видаляти елементи """

    def delete(self, key):
        """ Видаляє заданий елемент у бінарному дереві

        :param key: Елемент, який потрібно видалити з бінарного дерева
        """
        self._delete_helper(self, key)

    @staticmethod
    def _delete_helper(root, key):
        """ Допоміжний рекурсивний метод, що видаляє з дерева вузол з
            заданим ключем, якщо такий ключ міститься у дереві.

        :param root: корінь піддерева у якому потрібно видалити заданий елемент
        :param key: ключ елемента, який потрібно видалити
        """

        node = root.search(key)  # Знаходимо вузол, який треба видалити

        if node is None or node.mIsRoot:  # Якщо шуканий елемент не міститься у дереві,
            return                        # то припиняємо роботу підпрограми

        if node.hasNoChildren():          # Якщо знайдений вузол - листок (немає нащадків)
            isLeft = node.isLeftChild()   # Запам'ятаємо, яким сином по відношенню до батьківського є вузол, що видаляється
            node.removeSelfFromParent()   # Видаляємо вузол
            AVLTreeWithDelete.updateBalanceOnDelete(node.mParent, isLeft)  # Оновлюємо баланс батьківського вузла

        elif node.hasLeft() and not node.hasRight():  # Якщо знайдений вузол має лише одну ліву гілку
            node.setNode(node.mLeftChild)             # Замінюємо знайдений вузол його лівим піддіревом
            AVLTreeWithDelete.updateBalanceOnDelete(node.mParent, node.isLeftChild())

        elif node.hasRight() and not node.hasLeft():  # Якщо знайдений вузол має лише одну праву гілку
            node.setNode(node.mRightChild)            # Замінюємо знайдений вузол його правим піддіревом
            AVLTreeWithDelete.updateBalanceOnDelete(node.mParent, node.isLeftChild())

        else:                                         # Якщо знайдений вузол має обидві гілки
            left_max = AVLTreeWithDelete._search_max(node.mLeftChild)  # Знаходимо максимальний вузол у лівому піддереві
            left_max_key = left_max.mKey
            node.setNode(left_max_key)                # Замінюємо значення елемета node знайденим максимальним
            AVLTreeWithDelete._delete_helper(node.mLeftChild, left_max_key)  # Видалення з лівого піддерева найбільшого елементу

    @staticmethod
    def updateBalanceOnDelete(node, came_from_left):
        """ Оновлює баланс для поточно вузла при операції видалення

        :param node: вузол у якому потрібно оновити баланс
        :param came_from_left: від якого, лівого чи правого сина ми піднялися у вузол
        """

        if node.mIsRoot:
            return

        # оновлюємо баланс вузла залежно від того з якого нащадка ми прийшли
        if came_from_left:            # якщо ми прийшли з лівого сина,
            node.mBalanceFactor -= 1  # то баланс у вузлі зменшується на 1
        else:                         # якщо ми прийшли з правого сина,
            node.mBalanceFactor += 1  # то баланс у вузлі збільшується на 1

        # Якщо після оновлення балансу, вузол розбалансувався
        if node.mBalanceFactor > 1 or node.mBalanceFactor < -1:
            AVLTree.rebalance(node)  # Проводимо балансування вузла
            node = node.mParent      # після балансування змінилася вершина за яку була підвішена розбалансована вершина

        if node.mBalanceFactor == 0:
            # Якщо фактор балансу скорегувався до нуля,
            # це значить, що дерево зменшило свою висоту і необхідно провести
            # оновлення балансу для предка поточної вершини
            AVLTreeWithDelete.updateBalanceOnDelete(node.mParent, node.isLeftChild())



