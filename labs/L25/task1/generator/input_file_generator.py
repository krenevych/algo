from random import randint

from source.T7_Graphs.P4_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P4_Weighted.L6_Dijkstra import Dijkstra
from source.T7_Graphs.P4_Weighted.__test_weighted import show_way

MAX_WEIGHT = 50


def generate(fname, vertices, edges):
    print(fname)
    edges_dict = {}

    for i in range(edges):
        frm = randint(0, vertices)
        to = randint(0, vertices)
        weight = randint(0, MAX_WEIGHT)
        if frm != to:
            edges_dict[(frm, to)] = weight

    while True:
        start = randint(0, vertices)
        finish = randint(0, vertices)
        if start != finish:
            break

    g = GraphForAlgorithms(True)
    for v in range(vertices + 1):
        g.addVertex(v)

    for key, val in edges_dict.items():
        g.addEdge(key[0], key[1], val)

    way, way_weight = Dijkstra(g, start, finish)
    show_way(way, way_weight, "Dijkstra algorithm                    ")

    with open(fname, "w") as f_out:
        print(vertices, len(edges_dict), file=f_out)
        print(start, finish, file=f_out)
        lst = list(edges_dict.keys())
        lst.sort()
        for key in lst:
            print(*key, edges_dict[key], file=f_out)

        if way is None:
            print("None", file=f_out)
            print("INF", file=f_out)
        else:
            print(*way, file=f_out)
            print(way_weight, file=f_out)

    return edges_dict


if __name__ == "__main__":
    # generate("input00.txt", 10, 30)
    # generate("input01.txt", 100, 500)
    # generate("input02.txt", 500, 2500)
    # generate("input03.txt", 500, 2500)
    # generate("input04.txt", 500, 2500)
    # generate("input05.txt", 500, 2500)
    # generate("input06.txt", 10, 20)
    # generate("input07.txt", 100, 300)
    # generate("input08.txt", 100, 300)
    # generate("input09.txt", 500, 1300)
    generate("input10.txt", 500, 1300)
    generate("input11.txt", 500, 5300)
    print("Data generation finished!")
