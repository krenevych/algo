# TODO: задача розв'язана динамічним програмуванням.
#  Не проходить на е-олімпі одни тесткейс по часу

W = int(input())
v = [0] + list(map(int, input().split()))
n = len(v) - 1

m = []
for i in range(n + 1):
    l1 = [0] * (W + 1)
    m.append(l1)

for i in range(1, n + 1):
    for j in range(W + 1):
        if v[i] > j:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = max(m[i - 1][j], m[i - 1][j - v[i]] + v[i])

print(m[n][W])