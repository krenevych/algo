n = int(input())

counter = 0
while n > 0:
    counter += n & 1
    n = n >> 1

print(counter)
