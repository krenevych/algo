"""
Пошук всіх тризначних чисел, сума цифр яких дорівнює заданиму числу
"""

n = int(input())
counter = 0                     # лічильник кількості чисел
for i in range(1, 10):          # Перебір сотень
    for j in range(10):         # Перебір десятків
        for k in range(10):     # Перебір одиниць
            if i + j + k == n:
                counter += 1

print(counter)