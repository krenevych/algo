if __name__ == '__main__':

    with open("input.txt") as infile:
        n = int(infile.readline())
        edges = 0
        for i in range(n):
            row = list(map(int, infile.readline().split()))
            # print(*row)
            for j in range(n):
                if row[j] > 0:
                    edges += 1

        print(edges)

