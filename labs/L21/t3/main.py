if __name__ == '__main__':

    with open("input.txt") as infile:
        n = int(infile.readline())
        k = int(infile.readline())

        for i in range(k):
            inp = list(map(int, infile.readline().split()))
            if inp[0] == 1:
                # Add edge
                print("Add edge:", inp[1], inp[2])
            elif inp[0] == 2:
                # Vertex
                print(f"Neighbours {inp[1]}: ")
