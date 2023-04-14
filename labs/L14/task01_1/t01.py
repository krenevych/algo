class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        if not self.empty():
            res = self.items.pop(0)
            return res

    def front(self):
        if not self.empty():
            return self.items[0]

    def size(self):
        return len(self.items)

    def empty(self):
        return self.size() == 0

    def clear(self):
        self.items.clear()


if __name__ == '__main__':

    with open("input.txt") as f:
        queue = Queue()
        while True:
            line = f.readline().strip()
            if line == "exit":
                print("bye")
                break

            commands = line.split()
            # print(commands)
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
