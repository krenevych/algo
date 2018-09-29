from source.T7_Graphs.P4.maze import showMaze, wave, drawWayInMatrix

WALL_CELL = "."  # Не прохідна клітина

def readMazeFromFile(aFileName, M):
    # Функція зчитуванння лабіринту з файлу
    maze = []   # Створення порожньої матриці для задавання лабіринту

    global WALL_CELL

    row0 = [WALL_CELL] * (M + 2)  # перший рядок матриці, що визначає верхіню стіну
    maze.append(row0)

    # Зчитуванння лабіринту з файлу
    with open(aFileName) as f:
        for str_row in f:
            # Перетворення рядка у список цілих чисел
            row = list(str_row.strip())

            if len(row) == 0: # Захист від зайвих рядків у кінці файлу
                break

            # додавання лівої та правої "стіни" лабіринту
            row.insert(0, WALL_CELL)
            row.append(WALL_CELL)

            maze.append(row)  # додавання рядка до лабіринту

    rowLast = [WALL_CELL] * (M + 2)  # останній рядок матриці, що визначає нижню стіну
    maze.append(rowLast)

    return maze  # Повертаємо створений лабіринт


if __name__ == "__main__":

    maze = readMazeFromFile("maze2.txt", 5)
    showMaze(maze)
    print()

    mazeM, source = wave(maze, (1, 1), WALL_CELL)

    wayMatrix = drawWayInMatrix(source, (1, 1), (5, 5), "Wave ")
    showMaze(wayMatrix)

