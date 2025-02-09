class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    # Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root: Node) -> int:
        # Initialize a variable to store the maximum path sum seen so far.
        self.max_sum = float('-inf')
        
        def helper(node: Node) -> int:
            # Base case: if node is None, return 0.
            if node is None:
                return 0
            
            # Recursively find the maximum branch sum for left and right children.
            left_sum = max(helper(node.left), 0)   # ignore negative sums
            right_sum = max(helper(node.right), 0) # ignore negative sums
            
            # Maximum path sum at the current node, considering both left and right branch.
            current_path_sum = node.data + left_sum + right_sum
            
            # Update the global maximum path sum.
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum sum branch that can be extended to this node's parent.
            return node.data + max(left_sum, right_sum)
        
        # Begin recursion from the root.
        helper(root)
        
        # Return the maximum path sum found.
        return self.max_sum
