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
        n = int(infile.readline())
        graph = []
        for i in range(n):
            row = list(map(int, infile.readline().split()))
            graph.append(row)

    return graph, n


def bfs(graph, s):
    n = len(graph)
    s = s - 1  # В умові вершини нумеруються з 1, а в нашому графі - з нуля
    dist = 0
    # visited = set()  # множина відвіданих вершин
    distances = [-1] * n
    q = Queue(55)
    q.enque(s)
    distances[s] = 0
    while not q.empty():
        cur = q.deque()
        # опрацювати і додати в чергу всіх не відвіданих сусідів вершини cur
        for neigbour in range(n):
            if graph[cur][neigbour] != 0:
                if neigbour == s:
                    return True
                if distances[neigbour] == -1:
                    q.enque(neigbour)
                    distances[neigbour] = distances[cur] + 1

    return False

def checkCycle(graph):
    n = len(graph)
    for start in range(n):  # для кожної вершини графу
                        # запускаємо пошук в глибину/шиниру,
                        # щоб перевірити чи повернемося ми в одну з відвіданих вершин
        if bfs(graph, start):
            return 1

    return 0


def main():
    graph, n = readGrapf()
    print(checkCycle(graph))


if __name__ == "__main__": main()
