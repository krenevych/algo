from source.T4.P42_Queue.Queue import Queue
from source.T4.P41_Stack.Stack import Stack

WALL_CELL = 0  # Не прохідна клітина лабіринту або його стіна

def readMazeFromFile(aFileName, M):
    # Функція зчитуванння лабіринту з файлу
    maze = []  # Створення порожньої матриці для задавання лабіринту

    global WALL_CELL

    row0 = [WALL_CELL] * (M + 2)  # перший рядок матриці, що визначає верхіню стіну
    maze.append(row0)

    # Зчитуванння лабіринту з файлу
    with open(aFileName) as f:
        for str_row in f:
            row = list(map(int, str_row.split()))    # Перетворення рядка у список цілих чисел

            if len(row) == 0:  # Захист від зайвих рядків у кінці файлу
                break

            # додавання лівої та правої "стіни" лабіринту
            row.insert(0, WALL_CELL)
            row.append(WALL_CELL)

            maze.append(row) # додавання рядка до лабіринту

    rowLast = [WALL_CELL] * (M + 2)  # останній рядок матриці, що визначає нижню стіну
    maze.append(rowLast)

    return maze # Повертаємо створений лабіринт

def showMaze(maze):
    # функція форматованого виведення матриці лабіринту
    for row in maze:
        for el in row:
            print("%7s" % (el,), end="")
        print()


def wave(maze, start, wall_cell):
    """ функція побудови хвильової матриці для лібіринту
        P54 зі стартовою точкою start
        wall_cell - символ, що позначає стіну лабіринта або непрохідну його клітину"""

    # P54 - матриця лабіринту
    # start - початкова позиція у лабіринті у вигляді кортежу (рядкок, стовпчик)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dy = [0, -1, -1, -1, 0, 1, 1, 1]

    n = len(maze)     # кількість рядків у матриці P54
    m = len(maze[0])  # кількість стовпчиків у матриці P54

    # створення та ініціалізація хвильової матриці
    # такої ж розмірності, що і матриця лабіринту
    waveMatrix = []
    for i in range(n):
        row = [-1] * m
        waveMatrix.append(row)

    # створення та ініціалізація sources-матриці
    # такої ж розмірності, що і матриця лабіринту
    sources = []
    for i in range(n):
        row = [None] * m
        sources.append(row)

    q = Queue()        # Створюємо чергу
    q.enqueue(start)  # Додаємо у чергу координати стартової клітини
    waveMatrix[start[0]][start[1]] = 0  # Відстань від стартової клітини до себе нуль

    while not q.empty():

        current = q.dequeue()  # Беремо перший елемент з черги
        i = current[0]  # координата поточного рядка матриці
        j = current[1]  # координата поточного стовчика матриці

        # Додаємо в чергу всі сусідні клітини
        for k in range (len(dx)):

            i1 = i+dy[k]  # координата рядка сусідньої клітини
            j1 = j+dx[k]  # координата стовпчика сусідньої клітини

            # які ще не були відвідані та у які можна пересуватися
            if waveMatrix[i1][j1] == -1 and maze[i1][j1] != wall_cell:
                q.enqueue((i1, j1))
                # Встановлюємо відстань на одиницю більшу ніж для поточної
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1

                # Встановлюємо координати звідки ми прийшли у клітину
                sources[i1][j1] = (i, j)

    # Повертаємо хвильову матрицю, та sources-матрицю
    return waveMatrix, sources


def showWay(source, start, end, TAG):
    # функція виведення шляху

    # будуємо шлях за допомогою стеку
    stack = Stack()
    current = end
    while True:
        stack.push(current)
        if current == start:
            break
        current = source[current[0]][current[1]]
        if current is None:
            print(TAG, ": The way doesn't exist")
            return

    # виводимо шлях на екран
    while not stack.empty():
        v = stack.pop()
        if not stack.empty():
            print(v, end=" -> ")
        else:
            print(v)


def drawWayInMatrix(source, start, end, TAG):
    # функція виведення шляху

    # будуємо шлях за допомогою стеку
    stack = Stack()
    current = end
    while True:
        stack.push(current)
        if current == start:
            break
        current = source[current[0]][current[1]]
        if current is None:
            print(TAG, ": The way doesn't exist")
            return

    n = len(source)  # кількість рядків у матриці P54
    m = len(source[0])  # кількість стовпчиків у матриці P54
    # створення та ініціалізація хвильової матриці
    # такої ж розмірності, що і матриця лабіринту

    matrix = []
    for i in range(n):
        row = [" . "] * m
        matrix.append(row)

    # виводимо шлях на екран
    if not stack.empty():
        v = stack.pop()
        matrix[v[0]][v[1]] = "=S="

    while not stack.empty():
        v = stack.pop()

        if stack.empty():
            matrix[v[0]][v[1]] = "=F="
        else:
            matrix[v[0]][v[1]] = "-@-"

    return matrix


if __name__ == "__main__":
    maze = readMazeFromFile("maze1.txt", 7)
    showMaze(maze)
    print()

    mazeM, source = wave(maze, (3, 3), WALL_CELL)

    showWay(source, (3, 3), (5, 5), "Wave ")
    wayMatrix = drawWayInMatrix(source, (3, 3), (5, 5), "Wave ")

    showMaze(wayMatrix)




