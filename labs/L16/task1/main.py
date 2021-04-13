class Tree:
    def __init__(self, key):
        self.key = key
        self.isLeaf = False
        self.children = {}

    def insertNode(self, key):
        node = Tree(key)
        self.children[key] = node

    def __contains__(self, item):
        return item in self.children

    def __getitem__(self, item):
        return self.children[item]

    def __str__(self):
        return str(self.key) +" -> "+ str(list(self.children.keys()))

    def insert(self, telNumber):
        cur = self

        if len(telNumber) == 0:
            return

        childId = telNumber[0]
        if childId not in self:
            self.insertNode(childId)

        child = self[childId]
        rest = telNumber[1:]

        if child.isLeaf or (len(child.children) != 0 and len(rest) == 0):
            return False
            

        if len(rest) == 0:
            child.isLeaf = True

        res = child.insert(rest)

        return res


if __name__ == "__main__":
    tree = Tree("+")
    print(tree.insert("12"))
    print(tree.insert("123"))
    pass