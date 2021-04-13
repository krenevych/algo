class Tree:
    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.parent = None

    def __str__(self):
        return str(self.key)

    def addChild(self, node):
        self.children[node.key] = node
        node.parent = self

    def depth(self):
        curr = self
        h = 0
        while curr != None:
            h += 1
            curr = curr.parent
        return h


def add(parent_key, child_key):
    global tree_nodes
    child = Tree(child_key)
    tree_nodes[child_key] = child
    parent = tree_nodes[parent_key]
    parent.addChild(child)

def lsa(key1, key2):
    global tree_nodes
    if key1 not in tree_nodes or key2 not in tree_nodes:
        return 0
    node1 = tree_nodes[key1]
    node2 = tree_nodes[key2]
    h1 = node1.depth()
    h2 = node2.depth()
    while h1 != h2:
        if h1 > h2:
            node1 = node1.parent
            h1 -= 1
        else:
            node2 = node2.parent
            h2 -= 1

    while node1 != node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1.key

tree_nodes = {}
with open("input.txt") as f:
    tree_nodes[1] = Tree(1)
    testNum = int(f.readline().strip())
    for i in range(testNum):
        line = f.readline().split()
        command = line[0]
        key1 = int(line[1])
        key2 = int(line[2])
        if command == "ADD":
            add(key1, key2)
        elif command == "GET":
            print(lsa(key1, key2))
