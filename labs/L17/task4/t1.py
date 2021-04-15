import sys

from source.T5_LinearStructure.P1_Stack.L_2_Stack_recursively import Stack


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

def leaves(tree: SearchTree):
    if tree == None:
        return

    if tree.left == None and tree.right == None:
        print(tree, end=" ")

    leaves(tree.left)
    leaves(tree.right)

def leaves2(tree: SearchTree):

    stack = Stack()
    stack.push(tree)

    while not stack.empty():
        cur = stack.pop()

        if cur.left ==  cur.right == None:
            print(cur, end=" ")

        if cur.right != None:
            stack.push(cur.right)
        if cur.left != None:
            stack.push(cur.left)



INF = 9999999999
tree = SearchTree(INF)
with open("input.txt") as f:
    line = f.readline()
    data = list(map(int, line.split()))
    for key in data[:-1]:
        tree.insert(key)

leaves2(tree.left)

