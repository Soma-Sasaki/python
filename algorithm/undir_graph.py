import graphviz

def connect(graph, i, j):
    graph[i][j] = 1
    graph[j][i] = 1

def pretty_print(graph, n):
    print("   ", end = "")
    for i in range(0, n):
        print(i, " ", end = "")
    print("")
    for i in range(0, n):
        print(i, " ", end = "")
        for j in range(0, n):
            print(graph[i][j], " ", end = "")
        print("")

if __name__ == "__main__":
    N = 5
    graph = [[0 for i in range(0, N)] for j in range(0, N)]
    connect(graph, 0, 1)
    connect(graph, 0, 4)
    connect(graph, 1, 2)
    connect(graph, 1, 3)
    connect(graph, 2, 3)
    pretty_print(graph, N)

class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = set()

    def to_string(self):
        return str(self.id) + ", adj = " + str(self.adj)

def connect(vertices, i, j):
    vertices[i].adj.add(j)
    vertices[j].adj.add(i)

if __name__ == '__main__':
    N = 5
    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))
    connect(vertices, 0, 1)
    connect(vertices, 0, 4)
    connect(vertices, 1, 2)
    connect(vertices, 1, 3)
    connect(vertices, 2, 3)
    for i in range(0, N):
        print(vertices[i].to_string())
