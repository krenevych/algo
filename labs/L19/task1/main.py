class Heap:
    def __init__(self, max_heap_size):
        pass

    def insert(self, key):
        print(f"insert {key}")

    def extract(self):
        print("extract: ", end="")
        return None


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
