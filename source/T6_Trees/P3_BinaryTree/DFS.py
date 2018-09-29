from source.T6_Trees.P3_BinaryTree.BinaryTree import BinaryTree


def DFS(tree: BinaryTree):
    """ Обхід бінарного дерева в глибину

    :param tree: Бінарне дерево
    :return: None
    """

    if tree.has_left():                   # якщо дерево має лівого нащадка
        DFS(tree.left_subtree())          # запускаємо DFS для лівого нащадка

    if tree.has_right():                  # якщо дерево має правого нащадка
        DFS(tree.right_subtree())         # запускаємо DFS для правого нащадка

    print(tree.node())                   # Опрацьовуємо корінь елемент


if __name__ == "__main__":
    B1 = BinaryTree(1, 11, 111)
    B3 = BinaryTree(3, 33, 333)
    B2 = BinaryTree(2, 22, B3)
    B = BinaryTree(item=0, left=B1, right=B2)

    DFS(B)
