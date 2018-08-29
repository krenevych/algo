# TODO: задача розв'язана повним перебором. Не проходить на е-олімпі одни тесткейс по часу

maxN = 100
a = [0] * maxN
t = [0] * maxN

N, K = map(int, input().split())
for i in range(N):
    a[i], t[i] = map(int, input().split())

minTime = 100500


def findMinTime(time, score, mission_num):
    global minTime

    if mission_num >= N:
        if score >= K and minTime > time:
            minTime = time
        return

    findMinTime(time, score, mission_num + 1)

    nextTime = time + t[mission_num]
    if nextTime < minTime:
        nextScore = score + a[mission_num]
        findMinTime(nextTime, nextScore, mission_num + 1)


findMinTime(0, 0, 0)

if minTime == 100500:
    print(-1)
else:
    print(minTime)