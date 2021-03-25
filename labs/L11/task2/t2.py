class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.stack_size = 0

    def empty(self):
        return self.top == None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.stack_size += 1
        print("ok")

    def pop(self):
        if self.empty():
            print("error")
            return

        top_item = self.top.item
        self.top = self.top.next
        self.stack_size -= 1
        print(top_item)

    def back(self):
        if self.empty():
            print("error")
            return

        print(self.top.item)

    def size(self):
        print(self.stack_size)

    def clear(self):
        self.top = None
        self.stack_size = 0
        print("ok")


with open("input.txt") as f:
    stack = Stack()
    while True:
        line = f.readline().strip()
        if line == "exit":
            print("bye")
            break

        commands = line.split()
        command = commands[0]
        if command == "push":
            stack.push(commands[1])
        elif command == "pop":
            stack.pop()
        elif command == "back":
            stack.back()
        elif command == "size":
            stack.size()
        elif command == "clear":
            stack.clear()
