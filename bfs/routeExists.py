'''
Given a directed graph, design an algorithm to find out whether there is a route between 2 nodes

design ideas: use bfs to determine if path exists
              input: origin and destination
              output: true or false
'''

class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = []

    def setChildren(self, list):
        self.children = list

from Queue import Queue

def routeExists(origin, destination):
    visited = []
    q = Queue()
    q.put(origin)

    while not q.empty():
        current = q.get()
        if current not in visited:
            for child in current.children:
                if child.key == destination.key:
                    return True
                q.put(child)
            visited.append(current)

    return False

if __name__ == "__main__":
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node12 = Node(12)

    # directed graph
    node4.setChildren([node5,node6, node8])
    node5.setChildren([node4])
    node6.setChildren([node7,node8])
    node8.setChildren([node6,node7])
    node12.setChildren([node6])

    # this route fails, does not exist
    print routeExists(node4,node12)

    # this route passes, it exists
    print routeExists(node4,node7)

'''
Graph Adjacency List:
4:  5,6,8
5:  4
6:  7,8
7:
8:  6,7
12: 6


OUTPUT:
False
True

'''
