from source.T6_Trees.P2_BinaryTree.L5_SearchTreeNoneRecurseImplementation import SearchTree


class AVLTree(SearchTree):

    def __init__(self, key=None, left=None, right=None):
        super().__init__(key, left, right)

        self.mBalanceFactor = 0
        self.mIsRoot = False

    def setLeft(self, item):
        """ Змінює лівого сина.

        :param item: Навантаження або піддерево
        :return: None
        """
        if isinstance(item, AVLTree):           # якщо item є деревом
            self.mLeftChild = item              # змінюємо все піддерево
        elif self.hasLeft():                    # якщо дерево містить лівого сина
            self.mLeftChild.setNode(item)       # замінюємо вузол
        else:                                   # якщо дерево немає лівого сина
            self.mLeftChild = AVLTree(item)     # створюємо дерево з вузлом item та робимо його лівим сином
        self.mLeftChild.mParent = self
        self.updateBalance(self.mLeftChild)     # оновлення балансу для предків вставленого вузла

    def setRight(self, item):
        """ Змінює правого сина

        :param item: Ключ або піддерево
        :return: None
        """
        if isinstance(item, AVLTree):            # якщо item є деревом
            self.mRightChild = item              # змінюємо все піддерево
        elif self.hasRight():                    # якщо дерево містить правого сина
            self.mRightChild.setNode(item)       # замінюємо вузол
        else:                                    # якщо дерево немає правого сина
            self.mRightChild = AVLTree(item)     # створюємо дерево з вузлом item та робимо його правим сином
        self.mRightChild.mParent = self
        self.updateBalance(self.mRightChild)     # оновлення балансу для предків вставленого вузла

    def isLeftChild(self):
        return self.mParent and self.mParent.mLeftChild == self

    def isRightChild(self):
        return self.mParent and self.mParent.mRightChild == self

    @staticmethod
    def updateBalance(node):
        if node.mBalanceFactor > 1 or node.mBalanceFactor < -1:
            AVLTree.rebalance(node)
            return

        if not node.mParent.mIsRoot:
            if node.isLeftChild():
                node.mParent.mBalanceFactor += 1
            elif node.isRightChild():
                node.mParent.mBalanceFactor -= 1

            if node.mParent.mBalanceFactor != 0:
                AVLTree.updateBalance(node.mParent)

    @staticmethod
    def rebalance(node):
        """ Здійснює балансування дерева у розбалансованій вершині.

        :param node: розбалансована вершина дерева
        """
        if node.mBalanceFactor < 0:  # дерево перевішує вправо
            if node.mRightChild.mBalanceFactor > 0:  # необхідне велике обертання
                AVLTree.rotateRight(node.mRightChild)
                AVLTree.rotateLeft(node)
            else:
                AVLTree.rotateLeft(node)
        elif node.mBalanceFactor > 0:  # дерево перевішує вправо
            if node.mLeftChild.mBalanceFactor < 0:  # необхідне велике обертання
                AVLTree.rotateLeft(node.mLeftChild)
                AVLTree.rotateRight(node)
            else:
                AVLTree.rotateRight(node)

    @staticmethod
    def rotateLeft(node):
        """ Здійснює мале ліве обертання заданої вершини
        :param node: вершина, що обертається
        """
        node_parent = node.mParent
        if node.isLeftChild():
            node_parent.mLeftChild = AVLTree.__rotateLeft(node)
        elif node.isRightChild():
            node_parent.mRightChild = AVLTree.__rotateLeft(node)

    @staticmethod
    def __rotateLeft(root):
        """ Для піддерева заданим коренем здійснює мале ліве обертання

        :param root: корінь піддерева
        :return: новий корінь піддерева після операції обертання
        """
        pivot = root.mRightChild   # вершина, навколо якої здійснюється обертання
        root.mRightChild = pivot.mLeftChild

        if pivot.mLeftChild:
            pivot.mLeftChild.mParent = root

        pivot.mLeftChild = root

        node_parent = root.mParent
        root.mParent = pivot
        pivot.mParent = node_parent

        # Оновлення фактору збалансованості
        root.mBalanceFactor = root.mBalanceFactor + 1 - min(0, pivot.mBalanceFactor)
        pivot.mBalanceFactor = pivot.mBalanceFactor + 1 + max(0, root.mBalanceFactor)

        return pivot

    @staticmethod
    def rotateRight(node):
        """ Здійснює мале праве обертання заданої вершини
        :param node: вершина, що обертається
        """
        node_parent = node.mParent
        if node.isLeftChild():
            node_parent.mLeftChild = AVLTree.__rotateRight(node)
        elif node.isRightChild():
            node_parent.mRightChild = AVLTree.__rotateRight(node)

    @staticmethod
    def __rotateRight(root):
        """ Для піддерева заданим коренем здійснює мале праве обертання

        :param root: корінь піддерева
        :return: новий корінь піддерева після операції обертання
        """
        pivot = root.mLeftChild  # вершина, навколо якої здійснюється обертання
        root.mLeftChild = pivot.mRightChild

        if pivot.mRightChild:
            pivot.mRightChild.mParent = root

        pivot.mRightChild = root

        node_parent = root.mParent
        root.mParent = pivot
        pivot.mParent = node_parent

        # Оновлення фактору збалансованості
        root.mBalanceFactor = root.mBalanceFactor - 1 - max(pivot.mBalanceFactor, 0)
        pivot.mBalanceFactor = pivot.mBalanceFactor - 1 + min(root.mBalanceFactor, 0)

        return pivot

