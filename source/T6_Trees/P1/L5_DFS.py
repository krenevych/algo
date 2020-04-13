from source.T6_Trees.P1.L3_Tree import createSampleTree


def DFS(root):
    """ Обхід дерева в глибину
    :param root: корінь дерева з якого починається обхід
    """

    print(root.key(), end=" -> ")  # Опрацьовуємо корінь

    # запускаємо DFS для всіх дітей кореня
    for child in root.getChildren():
        DFS(child)


if __name__ == "__main__":
    tree = createSampleTree()
    DFS(tree)
