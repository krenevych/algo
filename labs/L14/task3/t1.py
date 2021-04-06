class Deque:
    def __init__(self):
        pass

    def push_front(self, item):
        pass

    def push_back(self, item):
        pass

    def isEmpty(self):
        return True

    def pop_front(self):
        return None

    def pop_back(self):
        return None

    def front(self):
        return None

    def back(self):
        return None

    def size(self):
        return 0

    def clear(self):
        pass


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
