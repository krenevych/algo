class Stack:
    def __init__(self):
        self.stack = [0] * 100
        self.current = 0

    def push(self, item):
        self.stack[self.current] = item
        self.current += 1
        print("ok")

    def pop(self):
        self.current -= 1
        item = self.stack[self.current]
        print(item)

    def back(self):
        print(self.stack[self.current - 1])

    def size(self):
        print(self.current)

    def clear(self):
        self.current = 0
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

