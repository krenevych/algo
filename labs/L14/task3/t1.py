
SIZE = 20000
class Deque:
    def __init__(self):
        self.items = [0] * SIZE
        self.bg = SIZE // 2
        self.en = SIZE // 2

    def push_front(self, item):
        self.bg -= 1
        self.items[self.bg] = item
        print("ok")

    def push_back(self, item):
        self.items[self.en] = item
        self.en += 1
        print("ok")

    def isEmpty(self):
        return self.bg == self.en

    def pop_front(self):
        first = self.items[self.bg]
        self.bg += 1
        print(first)
        return first

    def pop_back(self):
        self.en -= 1
        last = self.items[self.en]
        print(last)
        return last

    def front(self):
        b = self.items[self.bg]
        print(b)
        return b

    def back(self):
        e = self.items[self.en - 1]
        print(e)
        return e

    def size(self):
        siz = self.en - self.bg
        print(siz)
        return siz

    def clear(self):
        self.bg = SIZE // 2
        self.en = SIZE // 2
        print("ok")


with open("input.txt") as f:
    queue = Deque()
    while True:
        line = f.readline().strip()
        if line == "exit":
            print("bye")
            break

        commands = line.split()
        command = commands[0]
        if command == "push_front":
            queue.push_front(commands[1])
        elif command == "push_back":
            queue.push_back(commands[1])
        elif command == "pop_front":
            queue.pop_front()
        elif command == "pop_back":
            queue.pop_back()
        elif command == "front":
            queue.front()
        elif command == "back":
            queue.back()
        elif command == "size":
            queue.size()
        elif command == "clear":
            queue.clear()
