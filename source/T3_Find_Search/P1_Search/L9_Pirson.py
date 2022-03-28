from random import shuffle

# створення таблиці
example_table = list(range(0, 256))
shuffle(example_table)


def hash8(message, table):
    hash = len(message) % 256
    for i in message:
        hash = table[(hash + ord(i)) % 256]
    return hash



if __name__ == '__main__':
    print(hash8("Hello, world!", example_table))
