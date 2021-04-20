class Heap:
    def __init__(self, max_heap_size):
        self.data = [0] * max_heap_size
        self.size = 1

    def insert(self, key):
        # print("insert")
        # self.data.append(key)
        self.data[self.size] = key
        self.size += 1
        self.siftUp()

    def extract(self):
        res = self.data[1]
        self.data[1] = self.data[self.size - 1]
        self.size -= 1
        # self.data.pop()
        self.siftDown()

        return res

    def siftUp(self):
        start = self.size - 1
        while start > 1:
            parent = start // 2
            if self.data[start] > self.data[parent]:
                self.swap(start, parent)
            else:
                break

            start = parent


    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def siftDown(self):
        start = 1
        while 2 * start <= self.size - 1:
            left = 2 * start
            right = left + 1
            maxChild = self.getMaxChild(left, right)
            if self.data[start] < self.data[maxChild]:
                self.swap(start, maxChild)
            else:
                break

            start = maxChild

    def getMaxChild(self, left, right):
        if right >= self.size:
            return left
        elif self.data[left] > self.data[right]:
            return left
        else:
            return right



with open("input.txt") as f:
    N = int(f.readline())
    heap = Heap(N + 1)
    for quarry in range(N):
        command = list(map(int, f.readline().split()))
        if command[0] == 0:
            heap.insert(command[1])
        elif command[0] == 1:
            print(heap.extract())
