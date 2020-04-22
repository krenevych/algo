###########################################################
###########################################################
from source.T6_Trees.P2_BinaryTree.L7_AVLTree_Delete import AVLTreeWithDelete
from source.T6_Trees.P2_BinaryTree.examples.DFS_height import DFS_height

if __name__ == "__main__":

    s = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    ]

    s_delete = [1, 2, 3, 4, 5]

    search_tree = AVLTreeWithDelete(9999999999999)
    search_tree.mIsRoot = True
    for item in s:
        search_tree.insert(item)

    print("=========  ADDED  ===========")

    h = DFS_height(search_tree)
    print("Search tree height =", h)

    error = 0
    for i in s:
        res = search_tree.search(i)
        if res == None:
            error += 1

    print("Search errors =", error)

    for elem in s_delete:
        search_tree.delete(elem)

    error = 0
    for i in s_delete:
             res = search_tree.search(i)
             if res != None:
                  error += 1

    print("Search after delete error =", error)