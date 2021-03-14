class PrefixTree:

    def __init__(self, key=None):
        self.key = key
        self.leaf = False
        self.hasChildren = False
        self.children = [None] * 10

    def add(self, branch):
        curr = self
        for c in branch:
            if curr.leaf:
                return False

            key = int(c)
            if curr.children[key] == None:
                curr.hasChildren = True
                curr.children[key] = PrefixTree(key)

            curr = curr.children[key]

        if curr.leaf or curr.hasChildren:
            return False

        curr.leaf = True

        return True


with open("input.txt") as f:
    testNum = int(f.readline())
    for i in range(testNum):
        phones = PrefixTree()
        phonesNum = int(f.readline())
        res = True
        for ph in range(phonesNum):
            phone = (f.readline()).strip()
            if not res: continue

            res = phones.add(phone)

        if res:
            print("YES")
        else:
            print("NO")
