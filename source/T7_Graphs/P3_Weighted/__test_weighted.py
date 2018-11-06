from source.T7_Graphs.P3_Weighted.L8_PlainGraph import PlainGraph, inputGraphWithRandomVertexPositions
from source.T7_Graphs.P2_Nonweighted.L4_Ways import waySearch, waySearchByWave
from source.T7_Graphs.P3_Weighted.L9_AStar import AStar
from source.T7_Graphs.P3_Weighted.L3_BelmanFord import BelmanFord, BelmanFordOptimized
from source.T7_Graphs.P3_Weighted.L6_Dijkstra import Dijkstra


def show_way(vertices, weight, tag):
    # виводимо шлях way на екран
    print(tag, "(%d): " % weight, end="")
    for i in range(len(vertices) - 1):
        print(vertices[i], end=" -> ")
    print(vertices[-1])


if __name__ == "__main__":  # Для тестування

    points = 1000
    edges = 9000

    #     g = GraphForAlgorithms(True)
    #     inputRandomGraph(g, points, edges)

    g = PlainGraph(False)
    inputGraphWithRandomVertexPositions(g, points, edges)

    startV = 2

    way, way_weight = waySearch(g, startV, points)
    show_way(way, way_weight, "Wave algorithm                        ")
    way, way_weight = waySearchByWave(g, startV, points)
    show_way(way, way_weight, "Wave algorithm                        ")
    print("===================")
    way, way_weight = BelmanFord(g, startV, points)
    show_way(way, way_weight, "Bellman-Ford algorithm                ")
    print("===================")
    way, way_weight = BelmanFordOptimized(g, startV, points)
    show_way(way, way_weight, "Optimization of Bellman-Ford algorithm")
    print("===================")
    way, way_weight = Dijkstra(g, startV, points)
    show_way(way, way_weight, "Dijkstra algorithm                    ")
    print("===================")
    way, way_weight = AStar(g, startV, points)
    show_way(way, way_weight, "AStar algorithm                       ")

