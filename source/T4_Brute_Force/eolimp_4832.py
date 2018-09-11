
# TODO: Треба доробити згідно з умовою задачі. Динамічне програмування здається реалізоване коректно.

W = int(input())
w = [0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))

n = len(w)

m = []
for i in range(n):
    m.append([0] * (W + 1))

for i in range(1, n):
    for j in range(W + 1):
        if w[i] > j:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = max(m[i - 1][j], m[i - 1][j - w[i]] + v[i])

print(m[n-1][W])

