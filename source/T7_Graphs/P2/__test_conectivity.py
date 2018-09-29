from source.T7_Graphs.P1.Graph import Graph, inputGraphNet
from source.T7_Graphs.P1.GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P2.Connectivity import checkStrongConnected, checkConnected

if __name__ == "__main__":
    ###### StrongConnected
    g_0 = Graph(True)  # Створюємо не орієнтований граф

    inputGraphNet(g_0)
    print(g_0)
    print(checkStrongConnected(g_0))

    ############### Connected
    g = GraphForAlgorithms(False)  # Створюємо орієнтований граф
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 0)
    g.add_edge(5, 4)
    g.add_edge(5, 2)
    g.add_edge(6, 7)

    print(checkConnected(g))
