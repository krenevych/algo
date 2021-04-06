class Queue:
    def __init__(self):
        self.items = [0] * 20000
        self.bg = 0
        self.en = 0

    def push(self, item):
        self.items[self.en] = item
        self.en += 1
        print("ok")

    def pop(self):
        first = self.items[self.bg]
        self.bg += 1
        print(first)
        return first

    def front(self):
        print(self.items[self.bg])
        return self.items[self.bg]

    def size(self):
        siz = self.en - self.bg
        print(siz)
        return siz

    def clear(self):
        self.bg = 0
        self.en = 0
        print("ok")



with open("input.txt") as f:
    queue = Queue()
    while True:
        line = f.readline().strip()
        if line == "exit":
            print("bye")
            break

        commands = line.split()
        command = commands[0]
        if command == "push":
            queue.push(commands[1])
        elif command == "pop":
            queue.pop()
        elif command == "front":
            queue.front()
        elif command == "size":
            queue.size()
        elif command == "clear":
            queue.clear()

