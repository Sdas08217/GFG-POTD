# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Your Function Should return True/False
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def isCBT(self, root, index, node_count):
        if not root:
            return True
        if index >= node_count:
            return False
        left = self.isCBT(root.left, 2 * index + 1, node_count)
        right = self.isCBT(root.right, 2 * index + 2, node_count)
        return left and right

    def isMaxHeap(self, root):
        if not root:
            return True
        # Leaf node
        if not root.left and not root.right:
            return True
        # Only left child
        if not root.right:
            return root.data >= root.left.data and self.isMaxHeap(root.left)
        else:
            # Both children
            left = root.data >= root.left.data
            right = root.data >= root.right.data
            return left and right and self.isMaxHeap(root.left) and self.isMaxHeap(root.right)

    def isHeap(self, root):
        node_count = self.countNodes(root)
        if self.isCBT(root, 0, node_count) and self.isMaxHeap(root):
            return True
        return False
