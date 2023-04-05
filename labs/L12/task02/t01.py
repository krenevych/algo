class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, elem):
        new_top = Node(elem)
        self.__size += 1
        new_top.next = self.__top
        self.__top = new_top

    def pop(self):
        if self.empty():
            # raise RuntimeError("Stack is empty")
            return "error"

        top_elem = self.back()
        self.__top = self.__top.next
        self.__size -= 1
        return top_elem

    def back(self):
        if self.empty():
            # raise RuntimeError("Stack is empty")
            return "error"

        return self.__top.item

    def empty(self):
        return self.__top is None

    def size(self):
        return self.__size

        # # лінійний підрахунок кількості елементів у стеку - важкий по часу
        # counter = 0
        # current: Node = self.__top
        # while current is not None:
        #     counter += 1
        #     current = current.next
        #
        # return counter

    def clear(self):
        self.__top = None
        self.__size = 0


if __name__ == '__main__':
    with open("input.txt") as f:
        stack = Stack()
        while True:
            line = f.readline().strip()
            if line == "exit":
                print("bye")
                break

            commands = line.split()
            # print(commands)
            command = commands[0]
            if command == "push":
                stack.push(commands[1])
                print("ok")
            elif command == "pop":
                el = stack.pop()
                print(el)
            elif command == "back":
                el = stack.back()
                print(el)
            elif command == "size":
                size = stack.size()
                print(size)
            elif command == "clear":
                stack.clear()
                print("ok")
