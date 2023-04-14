class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.bg = None
        self.en = None
        self.counter = 0

    def push(self, n):
        newNode = Node(n)
        if not self.empty():
            self.en.next = newNode
        else:
            self.bg = newNode

        self.en = newNode
        self.counter += 1


    def pop(self):
        if self.empty():
            return "error"

        front = self.bg.data
        if self.bg.next is None:
            self.en = None

        self.bg = self.bg.next
        self.counter -= 1
        return front

    def front(self):
        if self.empty():
            return "error"

        return self.bg.data

    def empty(self):
        # return self.counter == 0
        return self.bg is None

    def size(self):
        return self.counter

    def clear(self):
        self.bg = None
        self.en = None
        self.counter = 0


if __name__ == '__main__':

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
                print("ok")
            elif command == "pop":
                print(queue.pop())
            elif command == "front":
                print(queue.front())
            elif command == "size":
                print(queue.size())
            elif command == "clear":
                queue.clear()
                print("ok")


