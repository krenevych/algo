if __name__ == '__main__':

    graph = []
    with open("input.txt") as infile:
        n = int(infile.readline())
        for i in range(n):
            inp = list(map(int, infile.readline().split()))
            # print(inp)
            row = [0] * n
            for j in inp[1:]:
                row[j-1] = 1

            # print(*row)
            graph.append(row)

        for row in graph:
            print(*row)
