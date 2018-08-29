class Stack:
    """ Клас, що реалізує стек елементів
        на базі вбудованого  списку Python """

    def __init__(self):
        """ Конструктор
        """
        self.items = []

    def empty(self):
        """ Перевіряє чи стек порожній

        :return: True, якщо стек порожній
        """
        return len(self.items) == 0

    def push(self, item):
        """ Додає елемент у стек

        :param item: елемент, що додається у стек
        :return: None
        """
        self.items.append(item)

    def pop(self):
        """ Забирає верхівку стека
            Сам елемент при цьому прибирається зі стеку

        :return: Верхівку стеку
        """
        if self.empty():
            raise Exception("Stack: 'pop' applied to empty container")
        return self.items.pop()

    def top(self):
        """ Повертає верхівку стека
            Сам елемент при цьому лишається у стеці

        :return: Верхівку стеку
        """

        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        return self.items[-1]

    def __len__(self):
        """ Розмір стеку

        :return: Розмір стеку
        """
        return len(self.items)

    def __str__(self):
        """ Перевизначає оператор "str()"
        :return: Зображення стека у виляді рядка
        """
        return  str(self.items)


# For testing
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

