class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    # Function to find the height of a binary tree.
    def height(self, root: Node) -> int:
        # Base case: if the node is None, return -1 (height of an empty tree is -1)
        if root is None:
            return -1
        
        # Recursively find the height of the left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # Return the maximum of the two heights plus 1 (for the current node)
        return max(left_height, right_height) + 1
