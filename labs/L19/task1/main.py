class Heap:
    def __init__(self, max_heap_size):
        self.data = [0] * max_heap_size
        self.size = 1

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)

    def insert(self, x):
        # print(f"Insert: {x}")
        self.data[self.size] = x
        self.size += 1
        self.siftUp()

    def siftUp(self):
        cur = self.size - 1
        while cur > 1:
            parent = cur // 2
            if self.data[cur] > self.data[parent]:
                self.swap(cur, parent)
            else:
                break

            cur = parent

    def swap(self, cur, parent):
        self.data[cur], self.data[parent] = self.data[parent], self.data[cur]

    def extract(self):
        max_elem = self.data[1]
        self.size -= 1
        self.data[1] = self.data[self.size]
        self.siftDown()
        return max_elem

    def siftDown(self):
        cur = 1
        while 2 * cur <= self.size - 1:
            maxChildIndex = self.getMaxChild(cur)
            if self.data[maxChildIndex] > self.data[cur]:
                self.swap(maxChildIndex, cur)
                cur = maxChildIndex
            else:
                break

    def getMaxChild(self, cur):
        left = 2 * cur
        right = 2 * cur + 1
        if right >= self.size:
            return left

        return left if self.data[left] > self.data[right] else right



if __name__ == '__main__':

    with open("input.txt") as f:
        N = int(f.readline())
        heap = Heap(N + 1)
        for quarry in range(N):
            command = list(map(int, f.readline().split()))
            if command[0] == 0:
                heap.insert(command[1])
            elif command[0] == 1:
                print(heap.extract())

    pass
