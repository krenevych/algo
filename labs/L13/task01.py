class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, elem):
        new_top = Node(elem)
        self.__size += 1
        new_top.next = self.__top
        self.__top = new_top

    def pop(self):
        if self.empty():
            # raise RuntimeError("Stack is empty")
            return "error"

        top_elem = self.back()
        self.__top = self.__top.next
        self.__size -= 1
        return top_elem

    def back(self):
        if self.empty():
            # raise RuntimeError("Stack is empty")
            return "error"

        return self.__top.item

    def empty(self):
        return self.__top is None

    def size(self):
        return self.__size


def getCharDigit(digit):
    """ Допоміжний метод, що за числом повертає символ-цифру системи числення

    0 -> '0'
    ...
    9 -> '9'
    10 -> 'A'
    ...
    15 -> 'F'

    :param digit: число з проміжку 0,.., 15
    :return: рядок що місить символ-цифру системи числення
    """

    assert digit <= 16
    if digit <= 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)

    return str_digit

# def binToDec(inBin: int):
#     por = 1
#     inDec = 0
#     while inBin > 0:
#         lastDig = inBin % 10
#         inDec += lastDig * por
#         inBin = inBin // 10
#         por *= 2
#     return inDec
#
# def toDec(D: int, BASE_FROM = 10):
#     por = 1
#     inDec = 0
#     while D > 0:
#         lastDig = D % 10
#         D = D // 10
#         inDec += lastDig * por
#         por *= BASE_FROM
#     return inDec
#
#
# def toOtherSystem(D: int, BASE_FROM=10, BASE_TO=10):
#     por = 1
#     res = 0
#     while D > 0:
#         lastDig = D % BASE_TO
#         D = D // BASE_TO
#         res += lastDig * por
#         por *= BASE_FROM
#     return res

def binToDecStr(inBin: str):
    por = 1
    inDec = 0
    for d in inBin[::-1]:
        inDec += int(d) * por
        por *= 2
    return inDec


def fromDec(D: int, BASE_TO=10):
    stack = Stack()

    while D > 0:
        lastDig = D % BASE_TO
        D = D // BASE_TO

        stack.push(getCharDigit(lastDig))

    res = ""
    while not stack.empty():
        top = stack.pop()
        res += top

    return res


if __name__ == '__main__':
    b = input()

    dec1 = binToDecStr(b)
    # print(dec1)

    hex1 = fromDec(dec1, BASE_TO=16)
    print(hex1)





