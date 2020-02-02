from source.T5_LinearStructure.P2_Queue.L1_Queue import Queue
from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.T7_Graphs.P4_Maizes.L1_Read import readMazeFromFile, showMaze, WALL_CELL


def wave(maze, start, wall_cell):
    """ функція побудови хвильової матриці для лібіринту зі стартовою точкою start

    :param maze: Матриця лабіринту
    :param start: Початкова точка лабіринту
    :param wall_cell: символ, що позначає стіну лабіринта або непрохідну його клітину
    :return: хвильову матрицю та sources-матрицю
    """

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dy = [0, -1, -1, -1, 0, 1, 1, 1]

    n = len(maze)     # кількість рядків у матриці maze
    m = len(maze[0])  # кількість стовпчиків у матриці maze

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

    q = Queue()       # Створюємо чергу
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

    n = len(source)  # кількість рядків у матриці P4_Maizes
    m = len(source[0])  # кількість стовпчиків у матриці P4_Maizes
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

    mazeM, source = wave(maze, (3, 3), WALL_CELL)

    showWay(source, (3, 3), (5, 5), "Wave ")
    wayMatrix = drawWayInMatrix(source, (3, 3), (5, 5), "Wave ")

    showMaze(wayMatrix)




