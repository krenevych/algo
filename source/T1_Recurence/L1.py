n = int(input("n = "))
a = 1                        # a = u
for k in range(1, n+1):
    a = k * a                # a = f(k, p, a)
print ("%d! = %d" % (n, a))  # виводимо на екран результат
