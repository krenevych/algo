# TODO: задача розв'язана динамічним програмуванням. Останні два тесткейси не проходять на е-олімпі - неправильна відповідь

INF = 10050000000
maxN = 105
w = [0] * maxN
v = [0] * maxN

n, W = map(int, input().split())
for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())

m = []
for i in range(n + 1):
    m.append([INF] * (W + 1))

for i in range(1, n + 1):
    for j in range(W + 1):
        if w[i] > j:
            m[i][j] = min(m[i - 1][j], v[i])
        else:
            m[i][j] = min(m[i - 1][j], v[i] + m[i - 1][j - w[i]])


if m[n][W-1] == INF:
    print(-1)
else:
    print(m[n][W-1])
