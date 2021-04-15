import sys


class SearchTree:

    NODE_COUNTER = -1

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        SearchTree.NODE_COUNTER += 1

    def __str__(self):
        return str(self.key)

    def insert(self, key):
        global NODE_COUNTER
        curr = self
        while True:
            if key == curr.key:
                return
            elif key > curr.key:
                if curr.right != None: # Вузол має правого сина
                    curr = curr.right
                else:
                    child = SearchTree(key)
                    curr.right = child
                    break

            elif key < curr.key:
                if curr.left != None:
                    curr = curr.left
                else:
                    child = SearchTree(key)
                    curr.left = child
                    break

def nodeCounting(tree: SearchTree):
    if tree:
        return 1 + nodeCounting(tree.left) \
               + nodeCounting(tree.right)

    return 0


INF = 9999999999
tree = SearchTree(INF)
with open("input.txt") as f:
    line = f.readline()
    data = list(map(int, line.split()))
    for key in data[:-1]:
        tree.insert(key)

# print(SearchTree.NODE_COUNTER)
print(nodeCounting(tree) - 1)