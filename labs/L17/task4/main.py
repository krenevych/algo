if __name__ == '__main__':
    with open("input.txt") as f:
        line = f.readline()
        data = list(map(int, line.split()))
        for key in data[:-1]:
            print(key)
            # TODO: implement insertion

