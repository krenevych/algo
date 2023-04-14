SIZE = 10000
class Deque:
    def __init__(self):
        self.items = [0] * SIZE
        self.b = SIZE // 2
        self.e = SIZE // 2

    def push_front(self, item):
        # print("push_front", end=": ")
        self.b -= 1
        self.items[self.b] = item
        print("ok")

    def push_back(self, item):
        # print("push_back", end=": ")
        self.items[self.e] = item
        self.e += 1
        print("ok")

    def empty(self):
        # print("isEmpty", end=": ")
        return self.b == self.e

    def pop_front(self):
        # print("pop_front", end=": ")
        if self.empty() : return "error"
        front = self.items[self.b]
        self.b += 1
        return front

    def pop_back(self):
        if self.empty() : return "error"
        # print("pop_back", end=": ")
        self.e -= 1
        return self.items[self.e]

    def front(self):
        if self.empty() : return "error"
        # print("front", end=": ")
        return self.items[self.b]

    def back(self):
        if self.empty() : return "error"
        # print("back", end=": ")
        return self.items[self.e - 1]

    def size(self):
        # print("size", end=": ")
        return self.e - self.b

    def clear(self):
        self.b = SIZE // 2
        self.e = SIZE // 2
        print("ok")


if __name__ == '__main__':
    with open("input.txt") as f:
        deque = Deque()
        while True:
            line = f.readline().strip()
            if line == "exit":
                print("bye")
                break

            commands = line.split()
            command = commands[0]
            if command == "push_front":
                deque.push_front(commands[1])
            elif command == "push_back":
                deque.push_back(commands[1])
            elif command == "pop_front":
                print( deque.pop_front())
            elif command == "pop_back":
                print( deque.pop_back())
            elif command == "front":
                print(deque.front())
            elif command == "back":
                print(deque.back())
            elif command == "size":
                print(deque.size())
            elif command == "clear":
                deque.clear()
