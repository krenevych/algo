
class Node:
    """ Допоміжний клас, що реалізує вузол стеку """

    def __init__(self, item):
        """ Конструктор

        :param item: навантаження вузла
        """
        self.mItem = item   # створюєм поле для зберігання навантаження
        self.mNext = None   # посилання на наступний вузол стеку


class Stack:
    """ Клас, що реалізує стек елементів
        як рекурсивну структуру """

    mTopNode: Node # Верхівка стеку

    def __init__(self):
        """ Конструктор
        """
        self.mTopNode = None  # посилання на верхівку стеку

    def empty(self) -> bool:
        """ Перевіряє чи стек порожній

        :return: True, якщо стек порожній
        """
        return self.mTopNode is None

    def push(self, item):
        """ Додає елемент у стек

        :param item: елемент, що додається у стек
        :return: None
        """

        new_node = Node(item)              # Створюємо новий вузол стеку
        if not self.empty():               # Якщо стек не порожній, то новий вузол
            new_node.mNext = self.mTopNode  # має посилатися на поточну верхівку

        self.mTopNode = new_node  # змінюємо верхівку стека новим вузлом

    def pop(self):
        """ Забирає верхівку стека
            Сам вузол при цьому прибирається зі стеку

        :return: Навантаження верхівки стеку
        """
        if self.empty():   # Якщо стек порожній
            raise Exception("Stack: 'pop' applied to empty container")

        current_top = self.mTopNode         # запам'ятовуємо поточну верхівку стека
        item = current_top.mItem             # запам'ятовуємо навантаження верхівки
        self.mTopNode = self.mTopNode.mNext  # замінюємо верхівку стека наступним вузлом у стеці
        del current_top  # видаляємо запам'ятований вузол, що місить попередню верхівку стека

        return item

    def top(self):
        """ Повертає верхівку стека
            Сам вузол при цьому лишається у стеці

        :return: Навантаження верхівки стеку
        """

        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        return self.mTopNode.mItem


# For testing
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)

    print(stack.top())
    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
