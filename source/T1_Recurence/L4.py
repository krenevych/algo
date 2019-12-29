n = int(input("n = "))
S = 1
for k in range(2, n + 1):
    S = 2 * S + k ** 2
print("S = ", S)
