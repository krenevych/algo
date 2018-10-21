from source.T6_Trees.P1.L3_Tree import Tree, createSampleTree


def DFS(tree):
    """ Обхід дерева в глибину
    :param tree: дерево
    """

    print(tree.key(), end=" -> ")  # Опрацьовуємо корінь

    # запускаємо DFS для всіх дітей кореня
    for child in tree.getChildren():
        DFS(child)


if __name__ == "__main__":
    tree = createSampleTree()
    DFS(tree)
