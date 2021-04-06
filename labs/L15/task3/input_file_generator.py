from random import randint

commands = [
    "empty",
    "set_first",
    "set_last",
    "next",
    "prev",
    "current",
    "insert_after",
    "insert_before",
    "delete"
]

def generate(fname, commands_number):
    f_out = open(fname, "w")
    N_MAXKEY = len(commands) - 1
    for i in range(commands_number):
        key = randint(0, N_MAXKEY)
        command = commands[key]
        print(command, file=f_out, end="")
        if command == "insert_after" or command == "insert_before":
            item = randint(0, 100500)
            print(" ", item, file=f_out, end="")
        print(file=f_out)
    f_out.close()


if __name__ == "__main__":
    generate("input01.txt", 100)
    generate("input02.txt", 500)
    generate("input04.txt", 1000)
    generate("input03.txt", 10000)
    generate("input05.txt", 100000)
