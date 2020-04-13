from source.T5_LinearStructure.P2_Queue.L1_Queue import Queue
from source.T6_Trees.P1.L3_Tree import createSampleTree


def BFS(root):
    """ Обхід дерева в ширину

    :param root: корінь дерева з якого починається обхід
    """
    q = Queue()      # Черга для опрацьованих вузлів
    q.enqueue(root)  # Додаємо у чергу корінь дерева

    while not q.empty():               # Поки черга не порожня
        node = q.dequeue()             # Беремо перший вузол з черги
        print(node.key(), end=" -> ")  # Опрацьовуємо взятий вузол

        # Додаємо в чергу всіх дітей поточного вузла
        for child in node.getChildren():
            q.enqueue(child)


# Головна програма
if __name__ == "__main__":
    tree = createSampleTree()  # підпрограма створення дерева
    BFS(tree)                  # запуск обходу в ширину
