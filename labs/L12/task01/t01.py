if __name__ == '__main__':

    with open("input.txt") as f:
        # stack = Stack()
        while True:
            line = f.readline().strip()
            if line == "exit":
                print("bye")
                break

            commands = line.split()
            print(commands)
            command = commands[0]
            if command == "push":
                # stack.push(commands[1])
                pass
            elif command == "pop":
                # stack.pop()
                pass
            elif command == "back":
                # stack.back()
                pass
            elif command == "size":
                # stack.size()
                pass
            elif command == "clear":
                # stack.clear()
                pass
