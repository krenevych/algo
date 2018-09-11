from random import Random

# from source.utils.benchmark import benchmark


def find1(a, n, s):
    for i in range(n):
        if a[i] == s:
            return True
    return False


# @benchmark
def find(a, n, s):
    i = 0
    while i < n:
        if a[i] == s:
            return True, i
        i += 1
    return False, i



import time

def find2(a, n, s):
    res = False
    i = 0
    while i < n:
        if a[i] == s:
            res = True
        i += 1
    return res

def H(n):
    res = 0
    i = 1
    while i < n:
        res += 1 / i
        i += 1
    return res


def constructArray(n):
    rnd = Random()
    a = [0] * n
    i = 0
    while i < n:
        s = rnd.randint(0, 2 * n)
        if s in a:
            continue

        a[i] = s
        i+=1

    return a

def constructArray1(n):
    rnd = Random()
    a = [0] * n
    for i in range(n):
        a[i] = i

    for i in range(n):
        j = rnd.randint(0, n-1)
        k = rnd.randint(0, n-1)
        a[k], a[j] = a[j], a[k]

    return a

def Experiment(n):
    rnd = Random()
    s = rnd.randint(0, 4 * n)
    a = constructArray1(n)

    t = time.clock()  # вимірюємо час перед викликом функції
    res, k = find(a, n, s)
    t1 = time.clock() - t  # вимірюємо різницю у часі після виклику функції

    t = time.clock()  # вимірюємо час перед викликом функції
    find2(a, n, s)
    t2 = time.clock() - t  # вимірюємо різницю у часі після виклику функції
    # print('Find2 : {:.8f}'.format(t2))

    return t1, t2, k

if __name__ == "__main__":   # Для тестування
    n = 1000
    # n = int(input())
    m = 200

    # print("[", end="")
    av_t1 = 0
    av_t2 = 0
    k = 0
    for i in range(m):
        t1, t2, k1 = Experiment(n)
        av_t1 += t1
        av_t2 += t2
        k += k1
        # if i % 5 == 0:
        #     print(".", end="")

    # print("]")

    av_t1 /= m
    av_t2 /= m
    k /= m

    print('Find  : {:.8f}'.format(av_t1))
    print('Find2 : {:.8f}'.format(av_t2))
    print('%%%   : {:.8f}'.format(av_t1 / av_t2))
    print('k     : {}'.format(k))
    # print('H     : {}'.format(H(n)))
