def Fib(n):
    if n == 0 or n == 1:                # Термінальна гілка
        return 1                        # Тривіальне значення
    else:                               # Рекурсивна гілка
        return Fib(n - 1) + Fib(n - 2)  # Рекурсивний виклик


# Виклик рекурсивної функції
n = int(input("n = "))
print("Fib(%d) = %d" % (n, Fib(n)))
