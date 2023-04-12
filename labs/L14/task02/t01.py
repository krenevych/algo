
class Queue:
    def __init__(self):
        pass

    def push(self, n):
        pass

    def pop(self):
        return 0

    def front(self):
        return 0

    def size(self):
        return 0

    def clear(self):
        pass


if __name__ == '__main__':

    with open("input.txt") as f:
        queue = Queue()
        while True:
            line = f.readline().strip()
            if line == "exit":
                print("bye")
                break

            commands = line.split()
            print(commands)
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


