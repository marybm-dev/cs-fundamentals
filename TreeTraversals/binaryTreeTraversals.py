

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def setChildren(self, left, right):
        self.left_child = left
        self.right_child = right

def visit(node):
    if node:
        print node.key

def preOrder(node):
    if node:
        visit(node)
        preOrder(node.left_child)
        preOrder(node.right_child)

def inOrder(node):
    if node:
        inOrder(node.left_child)
        visit(node)
        inOrder(node.right_child)

def postOrder(node):
    if node:
        postOrder(node.left_child)
        postOrder(node.right_child)
        visit(node)

if __name__ == "__main__":
    node18 = Node(18)
    node12 = Node(12)
    node30 = Node(30)
    node3 = Node(3)
    node15 = Node(15)
    node22 = Node(22)
    node49 = Node(49)
    node1 = Node(1)
    node8 = Node(8)
    node17 = Node(17)
    node44 = Node(44)

    node18.setChildren(node12, node30)
    node12.setChildren(node3, node15)
    node30.setChildren(node22, node49)
    node3.setChildren(node1, node8)
    node15.setChildren(None, node17)
    node49.setChildren(node44, None)

    print "Pre Order:"
    preOrder(node18)
    print "---------------------------------------------------"

    print "In Order:"
    inOrder(node18)
    print "---------------------------------------------------"

    print "Post Order:"
    postOrder(node18)
