class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root: Node, k: int) -> int:
        stack = []
        current = root
        count = 0
        
        # Iterative in-order traversal
        while stack or current:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current is now None; process the node at top of stack
            current = stack.pop()
            count += 1
            
            # If count equals k, we've found our kth smallest element.
            if count == k:
                return current.data
            
            # Move to the right subtree
            current = current.right
        
        # If we finish the traversal without finding kth element, return -1.
        return -1
