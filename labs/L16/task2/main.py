def add(parent_key, child_key):
    print(f"ADD: parent_key = {parent_key}, child_key = {child_key}")


def lsa(key1, key2):
    print(f"GET: key1 = {key1}, key2 = {key2}")
    # return lsa


if __name__ == '__main__':
    with open("input.txt") as f:
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
