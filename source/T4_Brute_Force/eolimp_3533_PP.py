# TODO: задача розв'язана повним перебором з застосуванням методу гілок і границь.
#  Не проходить на е-олімпі по часу

minTime = 100500   # рекорд

def findMinTime(time, score, mission_num):
    """
    :param time:        поточне значення часу
    :param score:       поточний рахунок
    :param mission_num: номер місії
    """
    global minTime  # глобальна змінна, що містить рекорд

    # Термінальна гілка, якщо опрацьовані всі місії
    if mission_num >= N:
        # Якщо значення цільової функції на знайденому розв’язку є меншим за рекорд
        if score >= K and minTime > time:
            minTime = time  # зміна рекорду
        return

    # рекурсивний виклик без урахуванням місії mission_num
    findMinTime(time, score, mission_num + 1)

    nextTime = time + t[mission_num]
    # Якщо оцінка знизу не менша за рекорд, то підмножина може бути відкинута
    if nextTime >= minTime:
        return

    nextScore = score + a[mission_num]  # рахунок з урахування місії mission_num
    # рекурсивний виклик з урахуванням місії mission_num
    findMinTime(nextTime, nextScore, mission_num + 1)


# Головна програма


maxN = 100
a = [0] * maxN
t = [0] * maxN

# зчитування даних задачі
N, K = map(int, input().split())
for i in range(N):
    a[i], t[i] = map(int, input().split())


findMinTime(0, 0, 0)

if minTime == 100500:
    print(-1)
else:
    print(minTime)
