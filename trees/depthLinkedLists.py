'''
Given a binary tree, design an algorithm which creates a linked list of all nodes at each depth.
e.g. a tree with depth D, will have a D linked lists

ideas: use bfs since we can look directly at the next level's children
input: binary tree root node
output: list/array of linked lists
'''

# next define the LL node object
class LLNode(object):
    def __init__(self, btnode):
        self.btnode = btnode
        self.next = None

# then define the LList I will be using
class LList(object):
    def __init__(self):
        self.root = None

    def length(self):
        if not self.root:
            return 0
        count = 1
        current = self.root
        while current.next:
            current = current.next
            count += 1
        return count

    def add(self, llnode):
        if not self.root:
            self.root = llnode
            return
        current = self.root
        while current.next:
            current = current.next
        current.next = llnode

def depthLinkedLists(btroot):
    list = []
    current = LList()
    current.add(LLNode(btroot))

    while current.length() > 0:
        list.append(current)

        parents = current
        current = LList()
        left = None
        right = None

        for parent in parents:
            if parent.left:
                left = LLNode(parent.left)
            if parent.right:
                right = LLNode(parent.right)
            if left:
                current.add(left)
            if right:
                current.add(right)

    return list


from minHeightBST import createMinHeightBST
if __name__ == '__main__':
    nums = [1,3,5,6,7,8,12,14,50,61,99]
    root = createMinHeightBST(nums)
    list = depthLinkedLists(root)

    for node in list:
        print node.key