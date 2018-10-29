from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import BinaryTree, createSampleTree


def BFS(tree: BinaryTree):
    """ Обхід бінарного дерева в ширину

    :param tree: Бінарне дерево
    :return: None
    """
    q = Queue()
    q.enqueue(tree)  # Додаємо у чергу корінь дерева

    while not q.empty():
        current = q.dequeue()    # Беремо перший елемент з черги
        print(current.mKey)    # Опрацьовуємо взятий елемент

        # Додаємо в чергу лівий і правий сини поточного вузла
        if current.hasLeft():                # якщо поточний вузол має лівого сина
            q.enqueue(current.mLeftChild)   # додаємо у чергу лівого сина
        if current.hasRight():               # якщо поточний вузол має правого сина
            q.enqueue(current.mRightChild)  # додаємо у чергу правого сина


if __name__ == "__main__":
    B = createSampleTree()
    BFS(B)
