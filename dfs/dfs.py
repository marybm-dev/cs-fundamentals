

class Vertex:
    def __init__(self, key):
        self.key = key
        self.visited = False

    def setNeighbors(self, adjList):
        self.neighbors = adjList


def dfs_visit(adjList):
    for vertex in adjList:
        if not vertex.visited:
            print "     visited: " + vertex.key
            vertex.visited = True
            dfs_visit(vertex.neighbors)

def dfs(tree):
    for vertex in tree:
        if not vertex.visited:
            print "root: " + vertex.key
            vertex.visited = True
            if vertex.neighbors:
                dfs_visit(vertex.neighbors)


if __name__ == '__main__':
    tree = []

    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')
    F = Vertex('F')
    G = Vertex('G')
    H = Vertex('H')
    I = Vertex('I')

    A.setNeighbors([B, C])
    B.setNeighbors([A, D, E])
    C.setNeighbors([A, F])
    D.setNeighbors([B])
    E.setNeighbors([B, F])
    F.setNeighbors([C, E])
    G.setNeighbors(None)
    H.setNeighbors([I])
    I.setNeighbors([H])

    tree.append(A)
    tree.append(B)
    tree.append(C)
    tree.append(D)
    tree.append(E)
    tree.append(F)
    tree.append(G)
    tree.append(H)
    tree.append(I)

    dfs(tree)
