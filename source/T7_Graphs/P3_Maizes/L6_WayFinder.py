from source.T7_Graphs.P3_Maizes.L2_ShowMaze import showMaze
from source.T7_Graphs.P3_Maizes.L4_ReadMazeFromFile import readMazeFromFile
from source.T7_Graphs.P3_Maizes.L5_Wave import wave

di = [0, -1, 0, 1]  # Зміщення по рядках
dj = [-1, 0, 1, 0]  # Зміщення по стовпчиках

# dj = [-1, -1, 0, 1, 1, 1, 0, -1]  # Зміщення по рядках
# di = [0, -1, -1, -1, 0, 1, 1, 1]  # Зміщення по стовпчиках


def findWay(maze, start, end):
    """ Зображує шлях за допомогою матриці

    :param maze: Матриця лібіринту
    :param start: Початкова точка шляху
    :param end: Кінцева точка шляху
    :return: Матриця у якій умовно зображено шлях
    """
    waveMatrix = wave(maze, start)  # Будуємо хвильову матрицю лабіринту

    if waveMatrix[end[0]][end[1]] == -1:   # Кінцева точка не досяжна зі стартової - шляху не існує
        print("The way doesn't exist")
        return

    n = len(waveMatrix)  # кількість рядків у матриці maze
    m = len(waveMatrix[0])  # кількість стовпчиків у матриці maze

    # матриця на якій буде показано шлях
    matrix = []
    for i in range(n):
        row = [" . "] * m
        matrix.append(row)

    matrix[end[0]][end[1]] = " F "  # Позначаємо точку кінця шляху буквою F

    current = end  # Рух починаємо з кінця
    while True:
        if current == start:
            matrix[current[0]][current[1]] = " S "  # Позначаємо точку початку шляху буквою S
            break

        i = current[0]  # координата поточного рядка матриці
        j = current[1]  # координата поточного стовчика матриці

        for k in range(len(dj)):
            i1 = i + di[k]  # координата рядка сусідньої клітини
            j1 = j + dj[k]  # координата стовпчика сусідньої клітини

            current = None
            if waveMatrix[i1][j1] == waveMatrix[i][j] - 1:
                current = (i1, j1)     # Знайдено клітину з якої ми прийшли у поточну
                matrix[i1][j1] = " # " # Позначаємо проміжну точку шляху
                break

    return matrix


if __name__ == "__main__":
    maze = readMazeFromFile("maze.txt", 7)
    wayMatrix = findWay(maze, (3, 3), (7, 7))
    showMaze(wayMatrix)




