from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree, createSampleTree


def DFS_height(root: BinaryTree):
    """ Рекурсивний пошук висоти дерева

    :param root: Корінь бінарного дерева
    :return: Висоту дерева
    """

    right_h = 0
    left_h = 0

    if root.hasLeft():          # якщо дерево має лівого сина
        left_h = 1 + DFS_height(root.mLeftChild)    # запускаємо DFS для лівого сина

    if root.hasRight():         # якщо дерево має правого сина
        right_h = 1 + DFS_height(root.mRightChild)   # запускаємо DFS для правого сина

    return max(left_h, right_h)


if __name__ == "__main__":
    B = createSampleTree()
    res = DFS_height(B)
