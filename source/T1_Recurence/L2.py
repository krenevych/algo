n = int(input("n = "))
x = float(input("x = "))
a = 1
for k in range(1, n+1):
    a = x / k * a     # можна так: a *= x / k
print ("a = ", a)     # виводимо на екран результат
