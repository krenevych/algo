if __name__ == '__main__':

    with open("input.txt") as infile:
        n = int(infile.readline())
        k = int(infile.readline())

        graph = []
        for i in range(n + 1):
            graph.append([])

        for i in range(k):
            inp = list(map(int, infile.readline().split()))
            if inp[0] == 1:
                # Add edge
                # print("Add edge:", inp[1], inp[2])
                graph[inp[1]].append(inp[2])
                graph[inp[2]].append(inp[1])
            elif inp[0] == 2:
                # Vertex
                # print(f"Neighbours {inp[1]}: ")
                print(*graph[inp[1]])

        # for row in graph:
        #     print(*row)