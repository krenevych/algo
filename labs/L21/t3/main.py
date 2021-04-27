with open("input.txt") as infile:
    n = int(infile.readline())
    k = int(infile.readline())
    graph = []
    for i in range(n):
        graph.append([])

    for i in range(k):
        inp = list(map(int, infile.readline().split()))
        if inp[0] == 1:
            # Add edge
            source = inp[1]
            dest = inp[2]
            graph[source - 1].append(dest)
            graph[dest - 1].append(source)
        elif inp[0] == 2:
            # Vertex
            vert = inp[1] - 1
            print(*graph[vert])
