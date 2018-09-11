

def f(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
        return sum


def g(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i + f(i)
        return sum

def h(n):
    return f(n) + g(n)


w = "hash"
S = 0
for i in w:
    S += ord(i)
    print(ord(i))

print(S)
print(S % 11)

l = [38, 4, 42, 56, 5, 40]
x = sum(l)

print(x)
print(x % 11)

x = None

sd = dict()
