
def isPhoneConsistent(phone):
    # TODO: implement algorithm
    print(f"Phone number {phone}")
    return True


with open("input.txt") as f:
    testNum = int(f.readline())
    for i in range(testNum):

        phonesNum = int(f.readline())
        res = True
        for ph in range(phonesNum):
            phone = (f.readline()).strip()
            if not isPhoneConsistent(phone):
                res = False

        if res:
            print("YES")
        else:
            print("NO")
