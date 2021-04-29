
def readGrapf():
    with open("input.txt") as infile:
        n = int(infile.readline())
        graph = []
        for i in range(n):
            row = list(map(int, infile.readline().split()))
            graph.append(row)

    return graph, n


def dfs(graph, start):
    n = len(graph)
    start = start - 1  # В умові вершини нумеруються з 1, а в нашому графі - з нуля
    visited = [False] * n
    global cycle
    cycle = False
    __dfs(graph, start, visited, start)
    return cycle

def __dfs(graph, start, visited, globalStart):
    n = len(graph)
    visited[start] = True
    # print(start + 1)
    # для всіх не відвіданих сусідів вершини start запустити пошук в глибину
    for neigbor in range(n):
        if graph[start][neigbor] != 0:  # вершина neigbor є сусідом вершини start
            if neigbor == globalStart:
                global cycle
                cycle = True

            if not visited[neigbor]:    # вершина neigbor не була відвідана
                visited[neigbor] = True
                __dfs(graph, neigbor, visited, globalStart)


def checkCycle(graph):
    n = len(graph)
    for start in range(n):  # для кожної вершини графу
                        # запускаємо пошук в глибину/шиниру,
                        # щоб перевірити чи повернемося ми в одну з відвіданих вершин

        if dfs(graph, start):
            return 1

    return 0


def main():
    graph, n = readGrapf()
    print(checkCycle(graph))
    # dfs(graph, 5)

if __name__ == "__main__": main()
