'''
Given a sorted (increasing order) array with unique integers, write an algorithm to create
a minimal heigh binary search tree.

ideas: use binary search logic to insert nodes?
    input: array of nums in ascending order
    output: BST
'''

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = root

def createMinHeightBST(nums):
    return minHeightBST(nums, 0, len(nums) -1)

def minHeightBST(nums, imin, imax):
    if imax < imin:
        return None

    middle = (imin + imax) / 2

    node = Node(nums[middle])
    print node.key
    node.left = minHeightBST(nums, imin, middle-1)
    node.right = minHeightBST(nums, middle+1, imax)

    return node

if __name__ == "__main__":
    nums = [1,3,5,6,7,8,12,14,50,61,99]
    root = createMinHeightBST(nums)
    tree = Tree(root)

'''
OUTPUT (PRE-ORDER node insertion):
8
5
1
3
6
7
50
12
14
61
99
'''