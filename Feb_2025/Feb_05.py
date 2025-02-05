class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return None  # Base case: empty tree
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively call mirror on left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root  # Return the root of the mirrored tree
