import user

edges_dict = {}
start, end = 1, 2
way = []
dist = 0
WAY_NOT_EXIST = "WAY_NOT_EXIST"
INF = -1


def readGraph(input_file):
    global edges_dict, way, dist, start, end
    with open(input_file) as in_file:
        vertices, edges = map(int, in_file.readline().split())
        start, end = map(int, in_file.readline().split())
        user.init(vertices, edges)
        for e in range(edges):
            frm, to, weight = map(int, in_file.readline().split())
            edges_dict[(frm, to)] = weight
            user.addEdge(frm, to, weight)

        way = in_file.readline().rstrip()
        try:
            way = list(map(int, way.split()))
        except ValueError:
            way = WAY_NOT_EXIST

        dist = in_file.readline().rstrip()
        try:
            dist = int(dist)
        except ValueError:
            dist = INF


def test(input_file):
    print(input_file.split(".")[0], end=": ")

    global edges_dict, way, dist
    edges_dict = {}

    readGraph(input_file)

    user_dis = user.findDistance(start, end)

    if user_dis == dist:
        print("OK!")
    else:
        print("Fail!")


def main():
    for i in range(12):
        input_file = f"input{i:02}.txt"
        try:
            test(input_file)
        except FileNotFoundError:
            print(f"input file: \"{input_file}\" not found!")


if __name__ == "__main__": main()
