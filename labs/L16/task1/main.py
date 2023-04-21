class PrefixTree:
    def __init__(self, key):
        self.key = key
        self.children = {}  # ���� ����, ��������

    def addChild(self, tail):
        if len(tail) == 0:
            return

        key = tail[0]

        child = self.children.get(key)
        if child is None:
            child = PrefixTree(key)
            self.children[key] = child

        child.addChild(tail[1:])

    def __repr__(self):
        return f"{self.key}"


def checkPhone(root, phone):
    if len(phone) == 0:
        return len(root.children) == 0
    else:
        key = phone[0]
        child = root.children[key]
        return checkPhone(child, phone[1:])


if __name__ == '__main__':
    with open("input.txt") as f:
        testNum = int(f.readline())
        for i in range(testNum):
            phones = []
            phonesNum = int(f.readline())
            root = PrefixTree("#")
            for ph in range(phonesNum):
                phone = (f.readline()).strip()
                phones.append(phone)
                root.addChild(phone)

            if len(phones) != len(set(phones)):  # ��� ��� ���� �������! �� ���� ���� ���� ��������� ������ � ������
                print("NO")
            else:
                for phone in phones:
                    if not checkPhone(root, phone):
                        print("NO")
                        break
                else:
                    print("YES")
