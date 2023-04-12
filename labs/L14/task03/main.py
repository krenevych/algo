class Deque:
    def __init__(self):
        pass

    def push_front(self, item):
        print("push_front", end=": ")
        print("ok")

    def push_back(self, item):
        print("push_back", end=": ")
        print("ok")

    def empty(self):
        print("isEmpty", end=": ")
        return True

    def pop_front(self):
        print("pop_front", end=": ")
        return None

    def pop_back(self):
        print("pop_back", end=": ")
        return None

    def front(self):
        print("front", end=": ")
        return None

    def back(self):
        print("back", end=": ")
        return None

    def size(self):
        print("size", end=": ")
        return 0

    def clear(self):
        print("clear", end=": ")
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
