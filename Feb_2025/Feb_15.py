class Solution:
    def LCA(self, root, n1, n2):
        # Base case
        if not root:
            return None
        
        # Ensure n1 and n2 are values, not Node objects
        if isinstance(n1, Node):
            n1 = n1.data
        if isinstance(n2, Node):
            n2 = n2.data
        
        # If both nodes are smaller, LCA lies in the left subtree
        if n1 < root.data and n2 < root.data:
            return self.LCA(root.left, n1, n2)
        
        # If both nodes are greater, LCA lies in the right subtree
        if n1 > root.data and n2 > root.data:
            return self.LCA(root.right, n1, n2)
        
        # If one node is on the left and the other is on the right, or one of them is root
        return root
