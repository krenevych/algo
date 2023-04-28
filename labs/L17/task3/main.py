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

        curr = self
        global maximum, maximum2

        while curr is not None:
            if key < curr.key:

                if curr.left is None:  # у поточного вузла НЕМАЄ лівої дитини
                    if maximum2 < key:
                        maximum2 = key
                    curr.left = SearchTree(key)  # вставляємо новий вузол як ліву дитину поточного вузла
                    return True  # вставка відбувалася
                else:  # у поточного вузла є ліва дитина
                    curr = curr.left

            elif key > curr.key:
                if curr.right is None:  # у поточного вузла НЕМАЄ правої дитити
                    if maximum < key:
                        maximum2 = maximum
                        maximum = key
                    curr.right = SearchTree(key)  # вставляємо новий вузол як праву дитину поточного вузла
                    return True  # вставка відбувалася
                else:
                    curr = curr.right
            else:
                return False  # вставка не відбулася, бо в дереві вже є вузол з ключем key


maximum = -1000000000000000  # фіктивний максимум
maximum2 = -1000000000000000  # фіктивний максимум

if __name__ == '__main__':
    searchTree = SearchTree(
        100000000000000)  # корінь дерева з фіктивним ключем. Вважається, що він не є елементом дерева, а використовується лише для зручності, щоб не гратися окремо з порожнім деревом
    with open("input.txt") as f:
        line = f.readline()
        data = list(map(int, line.split()))
        for key in data[:-1]:
            # print(key)
            searchTree.insert(key)

        # print(maximum)
        print(maximum2)
