from source.T6_Trees.P2_BinaryTree.L8_AVLTree_Delete import AVLTreeWithDelete
from source.T6_Trees.P2_BinaryTree.examples.DFS_height import DFS_height


s = [i for i in range(1, 100000)]

s_excluded = []
s_delete = s[::2]

search_tree = AVLTreeWithDelete(9999999999999)
search_tree.mIsRoot = True

for item in s:
    if item not in s_excluded:
        search_tree.insert(item)

print("=========  ADDED  ===========")

h = DFS_height(search_tree)
print("Search tree height =", h)

print("=========== testBalance before delete ===========")
search_tree.testBalance()

error = 0
for i in s:
    res = search_tree.search(i)
    if i in s_excluded:
        if res != None:
            error += 1
    else:
        if res == None:
            error += 1

print("Search errors =", error)

for elem in s_delete:
    search_tree.delete(elem)

print("======= testBalance after delete ===========")
search_tree.testBalance()

error = 0
for i in s_delete:
    res = search_tree.search(i)
    if res != None:
        error += 1

h = DFS_height(search_tree)
print("Search tree height =", h)

print("Search after delete error =", error)