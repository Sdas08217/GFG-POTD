# Mirror Tree
class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Base case: if the root is None, return
        if root is None:
            return
        
        # Recursively mirror the left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left

  # Example usage
if __name__ == "__main__":
    # Constructing the following binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder traversal before mirroring:")
    inorder(root)
    print()

    # Create Solution object and call the mirror function
    sol = Solution()
    sol.mirror(root)

    print("Inorder traversal after mirroring:")
    inorder(root)
    print()
      
