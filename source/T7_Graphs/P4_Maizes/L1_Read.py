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



if __name__ == "__main__":
    maze = readMazeFromFile("maze1.txt", 7)
    showMaze(maze)





