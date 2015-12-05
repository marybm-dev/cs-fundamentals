

class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = []

    def setChildren(self, list):
        self.children = list

from Queue import Queue

def bfs(root):
    visited = []
    q = Queue()
    q.put(root)

    while not q.empty():
        current = q.get()

        if current not in visited:
            for child in current.children:
                q.put(child)
            visited.append(current)
            print current.key

if __name__ == "__main__":
    node5 = Node(5)
    node8 = Node(8)
    node12 = Node(12)
    node13 = Node(13)
    node20 = Node(20)

    # undirected graph so we have 2 edges per vertex
    node5.setChildren([node8,node12, node20])
    node8.setChildren([node5,node12])
    node12.setChildren([node5,node13])
    node13.setChildren([node12])

    bfs(node5)



'''
Graph Representation (undirected)
         5
       / | \
      8-12  20
         |
        13

OUTPUT:
5
8
12
20
13

'''
