class Tree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add(self, key):
        self.children.append(key)

    def childrenCount(self):
        return len(self.children)

    def __str__(self):
        return str(self.key) + ", " + str(self.value) + ": " + str(self.children)


aparat = [Tree(0, 0)]


def main():
    global aparat
    with open("input.txt") as f:
        clerksNum = int(f.readline())
        for clerk_key in range(1, clerksNum + 1):
            clerk_properties = list(map(int, f.readline().split()))
            clerk_value = clerk_properties[0]
            clerk = Tree(clerk_key, clerk_value)
            aparat.append(clerk)

            clerk_children_count = clerk_properties[1]
            clerk_childrens = clerk_properties[2:]
            for child in clerk_childrens:
                clerk.add(child)


def dfs(key, current_pay):
    global record, aparat

    clerk: Tree = aparat[key]
    new_pay = current_pay + clerk.value
    if new_pay > record:
        return

    if clerk.childrenCount() == 0:
        if new_pay < record:
            record = new_pay
    else:
        for child in clerk.children:
            dfs(child, new_pay)


if __name__ == "__main__":
    record = 100500

    main()
    dfs(1, 0)
    print(record)
