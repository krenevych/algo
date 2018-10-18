from source.T6_Trees.P1.L3_Tree import Tree, createSampleTree


def DFS(tree: Tree):
    """ Обхід дерева в глибину
    :param tree: дерево
    """
    # запускаємо DFS для всіх дітей кореня
    for child in tree.getChildren():
        DFS(child)

    print(tree.key(), end=" -> ")  # Опрацьовуємо корінь після опрацювання дітей


if __name__ == "__main__":
    tree = createSampleTree()
    DFS(tree)
