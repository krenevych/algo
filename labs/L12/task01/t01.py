
class Stack:

    def __init__(self):
        self.elems = [0] * 101
        self.top = 0

    def push(self, elem):
        self.elems[self.top] = elem
        self.top += 1

    def pop(self):
        # if self.empty():  # міститься у операції back()
        #     raise RuntimeError("Stack is empty")

        top_elem = self.back()
        self.top -= 1

        return top_elem

    def back(self):
        if self.empty():
            raise RuntimeError("Stack is empty")
        return self.elems[self.top - 1]

    def empty(self):
        return self.size() == 0

    def size(self):
        return self.top

    def clear(self):
        self.top = 0


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