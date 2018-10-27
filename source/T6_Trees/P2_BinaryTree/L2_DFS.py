from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree, createSampleTree


def DFS(tree: BinaryTree):
    """ Обхід бінарного дерева в глибину

    :param tree: Бінарне дерево
    :return: None
    """

    print(tree.item())            # Опрацьовуємо корінь елемент

    if tree.hasLeft():            # якщо дерево має лівого сина
        DFS(tree.leftChild())     # запускаємо DFS для лівого сина

    if tree.hasRight():           # якщо дерево має правого сина
        DFS(tree.rightChild())    # запускаємо DFS для правого сина


if __name__ == "__main__":
    B = createSampleTree()
    print(B)

    DFS(B)
