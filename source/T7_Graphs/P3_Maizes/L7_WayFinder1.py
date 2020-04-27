from source.T5_LinearStructure.P1_Stack.L_1_Stack import Stack
from source.T7_Graphs.P3_Maizes.L2_ShowMaze import showMaze
from source.T7_Graphs.P3_Maizes.L4_ReadMazeFromFile import readMazeFromFile
from source.T7_Graphs.P3_Maizes.L5_Wave import wave

di = [0, -1, 0, 1]  # Зміщення по рядках
dj = [-1, 0, 1, 0]  # Зміщення по стовпчиках


# dj = [-1, -1, 0, 1, 1, 1, 0, -1]  # Зміщення по рядках
# di = [0, -1, -1, -1, 0, 1, 1, 1]  # Зміщення по стовпчиках


def findWay(maze, start, end):
    """ Шукає шлях у лабіринті

    :param maze: Матриця лабіринту
    :param start: Початкова точка шляху
    :param end: Кінцева точка шляху
    :return: Список, клітин шляху
    """
    waveMatrix = wave(maze, start)  # Будуємо хвильову матрицю лабіринту

    if waveMatrix[end[0]][end[1]] == -1:  # Кінцева точка не досяжна зі стартової - шляху не існує
        return []

    stack = Stack()  # Будуємо шлях за допомогою стеку
    current = end    # Рух починаємо з кінця
    while True:
        stack.push(current)   # Вштовхуємо у стек поточку клітину шляху
        if current == start:  # Якщо поточка вершина шляху є стартовою
            break             # Усі клітини шляху містяться у стеку

        i = current[0]  # координата поточного рядка матриці
        j = current[1]  # координата поточного стовчика матриці

        for k in range (len(dj)):
            i1 = i + di[k]  # координата рядка сусідньої клітини
            j1 = j + dj[k]  # координата стовпчика сусідньої клітини

            # Шукаємо клітину з якої ми прийшли у поточну
            current = None
            if waveMatrix[i1][j1] == waveMatrix[i][j] - 1:
                current = (i1, j1)
                break

    # Відновлюємо шлях зі стеку
    way = []
    while not stack.empty():
        way.append(stack.pop())

    return way


if __name__ == "__main__":
    maze = readMazeFromFile("maze.txt", 7)
    way = findWay(maze, (3, 3), (7, 7))
    print(way)





