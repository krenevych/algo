
maze = []
square = 0
with open("input.txt") as input_file:
    n = int(input_file.readline().strip())
    print(n)
    for i in range(n):
        row = input_file.readline().strip()
        print(row)