class Queue:

    def __init__(self, size=100):
        self.elements = [0] * size
        self.size = size
        self.b = 0
        self.e = 0

    def empty(self):
        return self.e == self.b

    def enqueue(self, item):
        if self.e == self.size:
            raise Exception("Queue overflow!")
        self.elements[self.e] = item
        self.e += 1

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty!")
        begin = self.elements[self.b]
        self.b += 1
        return begin


if __name__ == '__main__':
    q = Queue(3)
    q.enqueue(5)
    q.enqueue(1)
    q.enqueue(7)
    q.enqueue(17)

    while not q.empty():
        print(q.dequeue())