class PrefixTree:

    def __init__(self, key=None):
        self.key = key
        self.leaf = False
        self.children = {}

    def add(self, branch):
        curr = self
        for key in branch:
            if curr.leaf:
                return False

            if key not in curr.children:
                curr.children[key] = PrefixTree(key)

            curr = curr.children[key]

        if len(curr.children) != 0:
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
