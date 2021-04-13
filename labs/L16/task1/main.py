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

    @staticmethod
    def insert(tree, telNumber):
        if len(telNumber) == 0:
            return

        childId = telNumber[0]
        if childId not in tree:
            tree.insertNode(childId)

        child = tree[childId]
        rest = telNumber[1:]
        if len(rest) == 0:
            child.isLeaf = True
        Tree.insert(child, rest)



if __name__ == "__main__":
    tree = Tree("+")
    Tree.insert(tree, "123")
    Tree.insert(tree, "133")
    Tree.insert(tree, "134")
    Tree.insert(tree, "143")
    pass