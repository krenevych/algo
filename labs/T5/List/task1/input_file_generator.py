from random import randint

commands = [
    "empty",
    "reset",
    "next",
    "current",
    "insert_after",
    "insert_before",
    "delete",
    "damp"
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
    generate("input.txt", 5000)
