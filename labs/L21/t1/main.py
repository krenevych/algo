

if __name__ == '__main__':

    with open("input.txt") as infile:
        n = int(infile.readline())

        for i in range(n):
            row = list(map(int, infile.readline().split()))
            for j in range(i, n):
                if row[j] > 0:
                    print(i + 1, j + 1)