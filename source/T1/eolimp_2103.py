# TODO: задача розв'язана динамічним програмуванням

W, n = map(int, input().split())
v = [0] + list(map(int, input().split()))
w = [1] * (n + 1)

m = []
for i in range(n + 1):
    m.append([0] * (W + 1))

for i in range(1, n + 1):
    for j in range(W + 1):
        if w[i] > j:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = max(m[i - 1][j], v[i] + m[i - 1][j - w[i]])

print(m[n][W])
