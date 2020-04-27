from source.T7_Graphs.P3_Maizes.L2_ShowMaze import showMaze


def readMazeFromFile(fileName, M):
    """ Функція зчитування лабіринту з текстового файлу

    :param fileName: ім'я текстового файлу, що містить лабіринт
    :param M: кількість стовпчиків у лабіринті
    :return: матриця лабіринту
    """
    maze = []  # Створення порожньої матриці для задавання лабіринту

    row0 = [0] * (M + 2)  # перший рядок матриці, що визначає верхіню стіну
    maze.append(row0)

    # Зчитуванння лабіринту з файлу
    with open(fileName) as f:
        for str_row in f:
            row = list(map(int, str_row.split()))  # Перетворення рядка у список цілих чисел

            if len(row) == 0:  # Захист від зайвих рядків у кінці файлу
                break

            row.insert(0, 0)   # додавання лівої "стіни" лабіринту
            row.append(0)      # додавання правої "стіни" лабіринту

            maze.append(row)   # додавання рядка до лабіринту

    rowLast = [0] * (M + 2)    # останній рядок матриці, що визначає нижню стіну
    maze.append(rowLast)

    return maze  # Повертаємо створений лабіринт


if __name__ == "__main__":
    maze = readMazeFromFile("maze.txt", 7)
    showMaze(maze)
