# Remove Half Nodes
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def RemoveHalfNodes(self, node):
        # Base case: If the tree is empty, return None
        if node is None:
            return None
        
        # Recursively remove half nodes in the left and right subtrees
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        # If the current node is a half node with only one child, return that child
        if node.left is None and node.right is not None:
            return node.right
        if node.right is None and node.left is not None:
            return node.left
        
        # If the current node is not a half node, return the current node
        return node

# Helper function to perform inorder traversal and collect the result
def inorder_traversal(root, result):
    if root is not None:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)

# Example usage
if __name__ == "__main__":
    # Construct the binary tree for the first example
    root1 = TreeNode(5)
    root1.left = TreeNode(7)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(2)
    
    # Create a Solution object
    sol = Solution()
    
    # Remove half nodes and get the modified tree
    new_root1 = sol.RemoveHalfNodes(root1)
    
    # Perform inorder traversal and print the result
    result1 = []
    inorder_traversal(new_root1, result1)
    print("Inorder traversal of modified tree:", result1)  # Output: [2, 5, 8]
    
    # Construct the binary tree for the second example
    root2 = TreeNode(2)
    root2.left = TreeNode(7)
    root2.right = TreeNode(5)
    
    # Remove half nodes and get the modified tree
    new_root2 = sol.RemoveHalfNodes(root2)
    
    # Perform inorder traversal and print the result
    result2 = []
    inorder_traversal(new_root2, result2)
    print("Inorder traversal of modified tree:", result2)  # Output: [7, 2, 5]
