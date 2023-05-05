if __name__ == '__main__':

    with open("input.txt") as infile:
        n = int(infile.readline())
        for i in range(n):
            inp = list(map(int, infile.readline().split()))
            print(inp)
