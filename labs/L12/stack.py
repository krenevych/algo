class Stack:

    def __init__(self, size=100):
        self.elements = [0] * size
        self.size = size
        self.top = 0

    def empty(self):
        return self.top == 0

    def push(self, item):
        if self.top == self.size:
            raise Exception("Stack overflow!")
        self.elements[self.top] = item
        self.top += 1
        pass

    def pop(self):
        if self.empty():
            raise Exception("Стек порожній")
        topelement = self.elements[self.top - 1]
        self.top -= 1
        return topelement


if __name__ == '__main__':
    stack = Stack(3)
    stack.push(9)
    stack.push(7)
    stack.push(4)
    stack.push(5)
