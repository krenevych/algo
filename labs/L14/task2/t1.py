class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.bg = None
        self.en = None
        self.qSize = 0

    def push(self, item):
        node = Node(item)
        if self.en != None:
            self.en.next = node
        else:
            self.bg = node

        self.en = node
        self.qSize +=1
        print("ok")

    def isEmpty(self):
        return self.bg == None

    def pop(self):
        if self.isEmpty():
            # raise RuntimeError("pop: Empty Queue")
            print("error")
            return

        first = self.bg.data

        self.bg = self.bg.next
        if self.bg == None:
            self.en = None

        self.qSize -=1
        print(first)
        return first


    def front(self):
        if self.isEmpty():
            # raise RuntimeError("pop: Empty Queue")
            print("error")
            return

        first = self.bg.data

        print(first)
        return first


    def size(self):
        print(self.qSize)
        return self.qSize

    def clear(self):
        self.bg = None
        self.en = None
        self.qSize = 0

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

