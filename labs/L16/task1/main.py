
if __name__ == '__main__':
    with open("input.txt") as f:
        testNum = int(f.readline())
        for i in range(testNum):

            phonesNum = int(f.readline())
            res = True
            for ph in range(phonesNum):
                phone = (f.readline()).strip()
                print(phone)
                # TODO: implement algorithm

            if res:
                print("YES")
            else:
                print("NO")
