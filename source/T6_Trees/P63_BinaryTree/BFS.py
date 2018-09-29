from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T6_Trees.P63_BinaryTree.BinaryTree import BinaryTree


def BFS(tree: BinaryTree):
    """ Обхід бінарного дерева в ширину

    :param tree: Бінарне дерево
    :return: None
    """
    q = Queue()
    q.enqueue(tree)  # Додаємо у чергу корінь дерева

    while not q.empty():
        current = q.dequeue()    # Беремо перший елемент з черги
        print(current.node())  # Опрацьовуємо взятий елемент

        # Додаємо в чергу лівий і правий нащадки поточного вузла
        if current.has_left():                      # якщо поточний вузол має лівого нащадка
            q.enqueue(current.left_subtree())   # додаємо у чергу лівого нащадка
        if current.has_right():                     # якщо поточний вузол має правого нащадка
            q.enqueue(current.right_subtree())  # додаємо у чергу правого нащадка


if __name__ == "__main__":
    B1 = BinaryTree(1, 11, 111)
    B3 = BinaryTree(3, 33, 333)
    B2 = BinaryTree(2, 22, B3)
    B = BinaryTree(item=0, left=B1, right=B2)

    BFS(B)
