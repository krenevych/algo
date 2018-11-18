from source.T7_Graphs.P1_Definitions.L5_Graph import Graph
from source.T7_Graphs.P2_Nonweighted.L8_Connectivity import checkConnected

if __name__ == "__main__":
    # ###### StrongConnected
    # g_0 = Graph(True)  # Створюємо не орієнтований граф
    #
    # inputGraphNet(g_0)
    # print(g_0)
    # print(checkStrongConnected(g_0))

    ############### Connected
    g = Graph()  # Створюємо неорієнтований граф

    g.addEdge(1, 2)  # ребро (1, 2)
    g.addEdge(1, 3)  # ребро (1, 3)
    g.addEdge(1, 4)  # ребро (1, 4)
    g.addEdge(2, 3)  # ребро (2, 3)
    g.addEdge(2, 5)  # ребро (2, 5)
    g.addEdge(3, 4)  # ребро (3, 4)
    g.addEdge(3, 5)  # ребро (3, 5)
    g.addEdge(3, 6)  # ребро (3, 6)
    g.addEdge(4, 6)  # ребро (4, 6)
    g.addEdge(5, 4)  # ребро (5, 4)
    g.addEdge(5, 6)  # ребро (5, 6)

    print(checkConnected(g))
