from math import log2

if __name__ == '__main__':
    k = 7
    k1 = log2(k - 1)
    k2 = int(k1)
    n = 1 << k2 + 1
    print(n)
