n = int(input("n = "))
F2 = 1
F1 = 1
for k in range(2, n + 1):
    F = F1 + F2
    F2 = F1
    F1 = F
print("F = ", F1)
