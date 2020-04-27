from source.T5_LinearStructure.P2_Queue.L1_Queue import Queue
from source.T7_Graphs.P3_Maizes.L2_ShowMaze import showMaze
from source.T7_Graphs.P3_Maizes.L4_ReadMazeFromFile import readMazeFromFile

di = [0, -1, 0, 1]  # Зміщення по рядках
dj = [-1, 0, 1, 0]  # Зміщення по стовпчиках

# dj = [-1, -1, 0, 1, 1, 1, 0, -1]  # Зміщення по рядках
# di = [0, -1, -1, -1, 0, 1, 1, 1]  # Зміщення по стовпчиках

def wave(maze, start):
    """ функція побудови хвильової матриці для лібіринту зі стартовою точкою start

    :param maze: Матриця лабіринту
    :param start: Стартова  точка - кортеж (r, c) - номери рядка та стовпчика відповідно
    :return: заповнена хвильова матриця
    """

    n = len(maze)     # кількість рядків у матриці maze
    m = len(maze[0])  # кількість стовпчиків у матриці maze

    # створення та ініціалізація хвильової матриці
    # такої ж розмірності, що і матриця лабіринту
    waveMatrix = []
    for i in range(n):
        row = [-1] * m
        waveMatrix.append(row)

    q = Queue()       # Створюємо чергу
    q.enqueue(start)  # Додаємо у чергу координати стартової клітини
    waveMatrix[start[0]][start[1]] = 0  # Відстань від стартової клітини до себе нуль

    while not q.empty():

        current = q.dequeue()  # Беремо перший елемент з черги
        i = current[0]  # координата поточного рядка матриці
        j = current[1]  # координата поточного стовчика матриці

        # Додаємо в чергу всі сусідні клітини
        for k in range (len(dj)):

            i1 = i + di[k]  # координата рядка сусідньої клітини
            j1 = j + dj[k]  # координата стовпчика сусідньої клітини

            # які ще не були відвідані та у які можна пересуватися
            if waveMatrix[i1][j1] == -1 and maze[i1][j1] != 0:
                q.enqueue((i1, j1))
                # Встановлюємо відстань на одиницю більшу ніж для поточної
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1

    # Повертаємо хвильову матрицю, та sources-матрицю
    return waveMatrix


if __name__ == "__main__":
    maze = readMazeFromFile("maze.txt", 7)
    waveMatrix = wave(maze, (3, 3))
    showMaze(waveMatrix)




