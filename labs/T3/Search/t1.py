
d = int(input())

count = 0
while d > 0:
    count += d & 1
    d = d >> 1

print(count)