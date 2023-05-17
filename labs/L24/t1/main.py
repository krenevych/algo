

with open("input.txt") as input_file:
    n = int(input_file.readline())
    print(n)
    for i in range(n):
        row = input_file.readline().strip()
        print(row)

    start_row, start_col = map(int, input_file.readline().split())
    print(start_row, start_col)
