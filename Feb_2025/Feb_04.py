class Solution:
    def diameter(self, root):
        # Initialize max diameter as a list to keep track of the max found so far
        self.max_diameter = 0
        
        # Helper function to compute height and update diameter
        def height(node):
            if not node:
                return 0  # Base case: height of empty node is 0
            
            # Recursively get heights of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the maximum diameter found so far
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of the subtree rooted at 'node'
            return 1 + max(left_height, right_height)
        
        height(root)  # Compute the height and update diameter
        
        return self.max_diameter  # Return the computed max diameter
