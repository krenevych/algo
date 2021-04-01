
def toDec(d: int):
    res = 0
    pow2 = 1
    while d > 0:
        last = d % 10
        res = res + pow2 * last
        pow2 *= 2
        d //= 10
    return res

def toDec2(d: str):
    res = 0
    for c in d:
        res = res * 2 + int(c)
    return res

def convertDigit(d: int):
    if d < 10:
        return str(d)
    elif d == 10:
        return 'A'
    elif d == 11:
        return 'B'
    elif d == 12:
        return 'C'
    elif d == 13:
        return 'D'
    elif d == 14:
        return 'E'
    elif d == 15:
        return 'F'

# 1234

class Stack:
    def __init__(self):
        self.stack = [0] * 100000
        self.current = 0

    def empty(self):
        return self.current == 0

    def push(self, item):
        self.stack[self.current] = item
        self.current += 1

    def pop(self):
        self.current -= 1
        item = self.stack[self.current]
        return item

def toHex(d: int, base: int):
    s = Stack()
    while d > 0:
        last = d % base
        d //= base
        last = convertDigit(last)
        s.push(last)

    res = ""
    while not s.empty():
        c = s.pop()
        res += c

    return res

b = input()
d = toDec2(b)
h = toHex(d, 16)
print(h)

