from source.T7_Graphs.P1_Definitions.L5_Graph import Graph, inputGraphNet
from source.T7_Graphs.P3_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P4_Conectivity.Connectivity import checkStrongConnected, checkConnected

if __name__ == "__main__":
    ###### StrongConnected
    g_0 = Graph(True)  # Створюємо не орієнтований граф

    inputGraphNet(g_0)
    print(g_0)
    print(checkStrongConnected(g_0))

    ############### Connected
    g = GraphForAlgorithms(False)  # Створюємо орієнтований граф
    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)
    g.addEdge(6, 7)

    print(checkConnected(g))
