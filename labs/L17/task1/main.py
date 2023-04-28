max_height = 0


class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        # return f"{self.key} : l{self.left}, r{self.right}"
        return f"{self.key}"

    def __repr__(self):
        return str(self)

    def search(self, key):
        curr = self
        while curr is not None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return True
        return False

    def insert(self, key):
        global max_height
        curr = self
        current_height = 0
        while curr is not None:
            if key < curr.key:
                current_height += 1
                if curr.left is None:  # у поточного вузла НЕМАЄ лівої дитини
                    if max_height < current_height:
                        max_height = current_height
                    curr.left = SearchTree(key)  # вставляємо новий вузол як ліву дитину поточного вузла
                    return True  # вставка відбувалася
                else:  # у поточного вузла є ліва дитина
                    curr = curr.left

            elif key > curr.key:
                current_height += 1
                if curr.right is None:  # у поточного вузла НЕМАЄ правої дитити
                    if max_height < current_height:
                        max_height = current_height
                    curr.right = SearchTree(key)  # вставляємо новий вузол як праву дитину поточного вузла
                    return True  # вставка відбувалася
                else:
                    curr = curr.right
            else:
                return False  # вставка не відбулася, бо в дереві вже є вузол з ключем key


# def dfs(root: SearchTree, current_height=0):
#     global max_height
#     if max_height < current_height:
#         max_height = current_height
#
#     # print(root)
#     if root.left is not None:
#         dfs(root.left, current_height + 1)
#     if root.right is not None:
#         dfs(root.right, current_height + 1)


if __name__ == '__main__':
    searchTree = SearchTree(
        100000000000000)  # корінь дерева з фіктивним ключем. Вважається, що він не є елементом дерева, а використовується лише для зручності, щоб не гратися окремо з порожнім деревом
    with open("input.txt") as f:
        line = f.readline()
        data = list(map(int, line.split()))
        for key in data[:-1]:
            # print(key)
            searchTree.insert(key)

    # dfs(searchTree)
    # print("max_height = ", max_height)
    print(max_height)
