import sys


class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.level = 0
        # self.parent = None

    def __str__(self):
        return str(self.key)

    def insert(self, key):
        global MAX_HEIGHT
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
                    child.level = curr.level + 1
                    if child.level > MAX_HEIGHT:
                        MAX_HEIGHT = child.level
                    break

            elif key < curr.key:
                if curr.left != None:
                    curr = curr.left
                else:
                    child = SearchTree(key)
                    curr.left = child
                    child.level = curr.level + 1
                    if child.level > MAX_HEIGHT:
                        MAX_HEIGHT = child.level
                    break


# def height(tree):
    # dfs(tree, 0)

# def dfs(tree: SearchTree, cur_height):
#     global MAX_HEIGHT
#     if MAX_HEIGHT < cur_height:
#         MAX_HEIGHT = cur_height
#
#     if tree.left:
#         dfs(tree.left, cur_height + 1)
#     if tree.right:
#         dfs(tree.right, cur_height + 1)


INF = 9999999999

MAX_HEIGHT = 0
tree = SearchTree(INF)
with open("input.txt") as f:
    line = f.readline()
    data = list(map(int, line.split()))
    for key in data[:-1]:
        tree.insert(key)

# height(tree)
print(MAX_HEIGHT)