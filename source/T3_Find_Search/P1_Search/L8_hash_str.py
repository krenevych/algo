N = 31  # Просте число, що не перевищує 255
M = 100007  # Кількість всіх можливих хешів


def H(S):
    h = 0
    for i in range(len(S)):
        h = h * N + ord(S[i])
    return h % M


print(H("hash"))
print(H("hsah"))
print(H("hsadfah"))