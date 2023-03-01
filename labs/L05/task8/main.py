
if __name__ == '__main__':

    n, k = map(int, input().split())
    coords = [int(el) for el in input().split()]

    l = 0
    r = coords[-1] - coords[0]

    while True:
        m = (l + r) // 2
        coords_of_current = coords[0]
        for i in range(1, k):
#             шукаємо найпершу позицію у списку координат після coords_of_current
#               якщо координати закінчилися, то брейк збільшуємо ліву межу


