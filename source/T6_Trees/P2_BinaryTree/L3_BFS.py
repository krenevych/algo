from source.T5_LinearStructure.P2_Queue.L1_Queue import Queue
from source.T6_Trees.P2_BinaryTree.L1_BinaryTree import createSampleTree


def BFS(root):
    """ Обхід бінарного дерева в ширину

    :param root: Корінь бінарного дерева
    """
    q = Queue()
    q.enqueue(root)  # Додаємо у чергу корінь дерева

    while not q.empty():
        node = q.dequeue()    # Беремо перший елемент з черги
        print(node.mKey)      # Опрацьовуємо взятий елемент

        # Додаємо в чергу лівий і правий сини поточного вузла
        if node.hasLeft():                # якщо поточний вузол має лівого сина
            q.enqueue(node.mLeftChild)    # додаємо у чергу лівого сина
        if node.hasRight():               # якщо поточний вузол має правого сина
            q.enqueue(node.mRightChild)   # додаємо у чергу правого сина


if __name__ == "__main__":
    B = createSampleTree()
    BFS(B)
