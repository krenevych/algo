# n - дипломів
# w, h - розміри
# [l, r] = [0, max{w, h}*n] - область розв'язку задачі
#
# на кожному кроці алгоритму:
# m = l + (r-l)/2  # m = (l + r) // 2
#
# по висоті кількість дипломів: m // h
# по ширині кількість дипломів: m // w
# отже всього дипломів на дошці висотою m буде (m // h) * (m // w)
# порівнюємо кількість дипломів, # що поміщаються з n та приймаємо
# рішення чи збільшити чи зменшити розмір дошки

if __name__ == '__main__':
    # w, h, n = [int(el) for el in input().split()]
    w, h, n = map(int, input().split())
    left = 0
    right = max(w, h) * n
    while right - left > 1:
        m = (left + right) // 2
        diplomas = (m // h) * (m // w)
        if diplomas < n:
            left = m
        else:
            right = m

    print(right)
