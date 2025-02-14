class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def findTarget(self, root: Node, target: int) -> bool:
        # Helper function to perform in-order traversal and collect node values.
        def inorder(node, arr):
            if node:
                inorder(node.left, arr)
                arr.append(node.data)
                inorder(node.right, arr)
        
        # Get sorted values from BST
        values = []
        inorder(root, values)
        
        # Use two pointers to check for a pair that sums to target
        left, right = 0, len(values) - 1
        while left < right:
            current_sum = values[left] + values[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return False
