n = 1000
k = 0

# 1
i = 0
while i < n:
    k += 1
    i += 1

# 2
i = 1
while i < n:
    k += 1
    i = i * 2

# 3
i = n - 1
while i != 0:
    k += 1
    i = i / 2

# 4
i = 0
while i < n:
    if i % 2 == 0:
        k += 1
    i += 1

# 5
i = 0
while i < n:
    j = 0
    while j < n:
        k += 1
        j += 1
    i += 1

# 6
i = 0
while i < n:
    j = i
    while j < n:
        k += 1
        j += 1
    i += 1

# 7
i = 0
while i < n:
    j = 0
    while j < i * i:
        k += 1
        j += 1
    i += 1
