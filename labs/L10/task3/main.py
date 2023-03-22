M = []
n = 0

record = 100500
def salary(valCurrent, worker, availableWorks):
    global M, n, record
    if worker == n:
        if valCurrent < record:
            record = valCurrent

    for work in availableWorks:
        worksLast = availableWorks.copy()
        worksLast.remove(work)
        cur = valCurrent + M[worker][work]
        if cur > record:  # Оптимізація - метод гілок та меж
            continue
        salary(cur, worker+1, worksLast)



if __name__ == '__main__':
    with(open("input.txt") as f):
        n = int(f.readline())
        for line in f:
            row = [int(el) for el in line.split()]
            M.append(row)

    # print(M)

    salary(valCurrent=0, worker=0, availableWorks=list(range(n)))
    print(record)

