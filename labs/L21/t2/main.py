with open("input.txt") as infile:
    n = int(infile.readline())
    # graph = []
    for i in range(n):
        inp = list(map(int, infile.readline().split()))
        row = [0] * n
        for j in inp[1:]:
            row[j - 1] = 1

        print(*row)
