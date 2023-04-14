class Queue:
    def __init__(self):
        self.items = [0] * 1000
        self.bg = 0
        self.en = 0

    def push(self, n):
        self.items[self.en] = n
        self.en += 1

    def pop(self):
        if not self.empty():
            res = self.items[self.bg]
            self.bg += 1
            return res

    def front(self):
        if not self.empty():
            return self.items[self.bg]

    def size(self):
        return self.en - self.bg

    def empty(self):
        return self.bg == self.en

    def clear(self):
        self.bg = 0
        self.en = 0


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
