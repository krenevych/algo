from source.T5_LinearStructure.P2_Queue.Queue import Queue
from source.T6_Trees.P1.L3_Tree import createSampleTree, Tree


def search(tree: Tree, elem: int) -> bool:
    """ Пошук заданого елемента у дереві
    Використовується пошук в ширину

    :param tree: дерево
    :param elem: шуканий елемент
    :return: True, якщо шуканий елемент міститься у дереві
    """

    q = Queue()      # Черга для опрацьованих вузлів
    q.enqueue(tree)  # Додаємо у чергу корінь дерева

    while not q.empty():           # Поки черга не порожня
        current = q.dequeue()      # Беремо перший елемент з черги
        if current.key() == elem:  # Якщо елемент знайдено
            return True            # Припиняємо пошук, повертаємо True

        # Додаємо в чергу всіх дітей поточного вузла
        for child in current.getChildren():
            q.enqueue(child)

    return False   # Повертаємо False – дерево не містить шуканого елементу


# Головна програма
if __name__ == "__main__":
    tree = createSampleTree()  # підпрограма створення дерева
    print(search(tree, 13))       # запуск обходу в ширину
