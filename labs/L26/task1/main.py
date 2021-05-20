from labs.L26.task1.PriorityQueue import PriorityQueue

INF = 100000000
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbour = {}  # список (словник ключ_вершини: вага ребра) сусідів
        self.distance = INF
        self.source = None  # використовується для побудови шляху - вершина з якої ми прийшли у поточну вершину

    def __str__(self):
        return str(self.key) + ":" + str(*self.neighbour.keys())


def main():
    graph = []
    with open("input.txt") as in_file:
        vertices, edges = map(int, in_file.readline().split())
        for i in range(vertices + 1):
            graph.append(Vertex(i))

        for e in range(edges):
            source, destination, weight = map(int, in_file.readline().split())
            graph[source].neighbour[destination] = weight
            graph[destination].neighbour[source] = weight

    weight = constractSpanningTree(graph)
    print(weight)


def constractSpanningTree(graph):

    for v in graph:
        v.distance = INF
        v.source = None

    start = 1

    graph[start].distance = 0
    pq = PriorityQueue()
    for key_ver in range(len(graph)):
        pq.insert(key_ver, graph[key_ver].distance)

    while not pq.empty():
        vert = pq.extractMinimum()

        for neigb, weight in graph[vert].neighbour.items():
            if neigb in pq and weight < graph[neigb].distance:
                graph[neigb].distance = weight
                graph[neigb].source = vert
                pq.updatePriority(neigb, graph[neigb].distance)

    return 0


if __name__ == "__main__": main()
