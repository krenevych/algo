def sum(a, n):
    result = a[0]
    i = 1
    while i < n:
        result += a[i]
        i += 1
    return result


def sumM(A, n):
    result = 0
    i = 0
    j = 0
    while i < n:
        while j < n:
            result += A[i][j]
            j += 1
        j = 0
        i += 1
    return result


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def S1(x, n):
    sum = 0
    i = 0
    while i <= n:
        prod = 1
        j = 0
        while j < i:
            prod *= x
            j += 1
        sum += prod
        i += 1
    return sum


def S2(x, n):
    sum = 0
    i = 0
    while i <= n:
        sum = sum * x + 1
        i += 1
    return sum


def pow1(x, n):
    result = 1
    i = 0
    while i <= n:
        result = result * x
        i += 1
    return result


def pow(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(x * x, n / 2)
    else:
        return x * pow(x*x, (n - 1) / 2)


print(pow(2, 16))
