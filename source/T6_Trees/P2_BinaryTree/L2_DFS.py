from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree, createSampleTree


def DFS(root: BinaryTree):
    """ Обхід бінарного дерева в глибину

    :param root: Корінь бінарного дерева
    :return: None
    """

    print(root.mKey)            # Опрацьовуємо корінь елемент

    if root.hasLeft():          # якщо дерево має лівого сина
        DFS(root.mLeftChild)    # запускаємо DFS для лівого сина

    if root.hasRight():         # якщо дерево має правого сина
        DFS(root.mRightChild)   # запускаємо DFS для правого сина


if __name__ == "__main__":
    B = createSampleTree()
    DFS(B)
