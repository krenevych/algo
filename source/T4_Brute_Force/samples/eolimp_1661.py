
# TODO: задача розв'язана динамічним програмуванням. Засабмічена на е-олімпі 100%

maxN = 36
ws = [0] * maxN
v = [0] * maxN

W, N = map(int, input().split())
for i in range(1, N + 1):
    ws[i], v[i] = map(int, input().split())

m = []
for i in range(N + 1):
    m.append([0] * (W + 1))

for i in range(1, N + 1):
    for w in range(W + 1):
        if w < ws[i]:
            m[i][w] = m[i - 1][w]
        else:
            m[i][w] = max(m[i - 1][w], v[i] + m[i][w - ws[i]])

print(m[N][W])
