class Queue:
    def __init__(self, size):
        self.q = [0] * size
        self.b = 0
        self.e = 0

    def enque(self, item):
        self.q[self.e] = item
        self.e += 1

    def deque(self):
        item = self.q[self.b]
        self.b += 1
        return item

    def empty(self):
        return self.b == self.e


def readGrapf():
    with open("input.txt") as infile:
        n, s,f = map(int, infile.readline().split())
        graph = []
        for i in range(n):
            row = list(map(int, infile.readline().split()))
            graph.append(row)

    return graph, n, s, f


def bfs(graph, s, f):
    n = len(graph)
    s = s - 1  # В умові вершини нумеруються з 1, а в нашому графі - з нуля
    f = f - 1
    dist = 0
    # visited = set()  # множина відвіданих вершин
    distances = [-1] * n
    q = Queue(105)
    q.enque(s)
    # visited.add(s)  # помічаємо стартову вершину як відвідану
    distances[s] = 0
    while not q.empty():
        cur = q.deque()
        # опрацювати і додати в чергу всіх не відвіданих сусідів вершини cur
        # print(cur + 1)
        for vertex in range(n):
            if graph[cur][vertex] != 0 and distances[vertex] == -1:
                q.enque(vertex)
                # visited.add(vertex)
                distances[vertex] = distances[cur] + 1

    return distances[f] if distances[f] != -1 else 0 # мінімальну відстань від початкової вершини s до кінцевої f

def main():
    graph, n, s, f = readGrapf()
    dist = bfs(graph, s, f)
    print(dist)

if __name__ == "__main__": main()
