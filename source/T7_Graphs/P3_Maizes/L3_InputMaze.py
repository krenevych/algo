from source.T7_Graphs.P3_Maizes.L2_ShowMaze import showMaze


def inputMaze(N, M):
    """ Функція зчитування лабіринту з клавіатури
    :param N: кількість рядків у лабіринті
    :param M: кількість стовчиків у лабіринті
    :return: матриця лабіринту
    """
    maze = []  # Створення порожньої матриці для задавання лабіринту

    row0 = [0] * (M + 2)     # перший рядок матриці, що визначає верхіню стіну
    maze.append(row0)

    for i in range(N):
        str_row = input()    # Зчитування рядка з клавіатури
        row = list(map(int, str_row.split()))  # Перетворення рядка у список цілих чисел
        row.insert(0, 0)     # додавання лівої "стіни" лабіринту
        row.append(0)        # додавання правої "стіни" лабіринту
        maze.append(row)     # додавання рядка до лабіринту

    rowLast = [0] * (M + 2)  # останній рядок матриці, що визначає нижню стіну
    maze.append(rowLast)

    return maze              # Повертаємо створений лабіринт



if __name__ == "__main__":
    maze = inputMaze(7, 7)
    showMaze(maze)
