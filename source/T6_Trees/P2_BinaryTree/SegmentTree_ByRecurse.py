class SegmentTree:

    def __init__(self):
        self.mSize = 0
        self.mItems = []

    def initialize(self, array):
        self.mSize = len(array)
        self.mItems = [0] * 4 * self.mSize
        self.__build(0, 0, self.mSize - 1, array)

    def __build(self, v, vl, vr, a):
        if vl == vr:
            self.mItems[v] = a[vl]
            return
        vm = (vl + vr) // 2
        self.__build(2 * v + 1, vl, vm, a)
        self.__build(2 * v + 2, vm + 1, vr, a)
        self.mItems[v] = self.mItems[2 * v + 1] + self.mItems[2 * v + 2]

    def __query(self, v, vl, vr, l, r):
        if r < vl or vr < l:
            return 0
        elif l <= vl and vr <= r:
            return self.mItems[v]
        else:
            vm = (vl + vr) // 2
            q1 = self.__query(2 * v + 1, vl, vm, l, r)
            q2 = self.__query(2 * v + 2, vm + 1, vr, l, r)
            return q1 + q2

    def getSum(self, l, r):
        return self.__query(0, 0, self.mSize - 1, l, r)


if __name__ == "__main__":
    a1 = [2, 7, 6, 4, 1, 3]

    segTree = SegmentTree()
    segTree.initialize(a1)

    res = segTree.getSum(1, 5)
    print(res)

    print(0)
