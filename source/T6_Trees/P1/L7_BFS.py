from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T6_Trees.P1.L3_Tree import createSampleTree, Tree


def BFS(tree):
    """ Обхід дерева в ширину

    :param tree: дерево
    """
    q = Queue()      # Черга для опрацьованих вузлів
    q.enqueue(tree)  # Додаємо у чергу корінь дерева

    while not q.empty():                  # Поки черга не порожня
        current = q.dequeue()             # Беремо перший елемент з черги
        print(current.key(), end=" -> ")  # Опрацьовуємо взятий елемент

        # Додаємо в чергу всіх дітей поточного вузла
        for child in current.getChildren():
            q.enqueue(child)


# Головна програма
if __name__ == "__main__":
    tree = createSampleTree()  # підпрограма створення дерева
    BFS(tree)                  # запуск обходу в ширину
