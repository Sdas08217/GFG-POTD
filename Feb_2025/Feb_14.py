class Solution:
    def __init__(self):
        self.first = self.middle = self.last = self.prev = None
    
    def inorder(self, root):
        if not root:
            return
        
        # Inorder traversal
        self.inorder(root.left)
        
        # Find swapped nodes
        if self.prev and root.data < self.prev.data:
            if not self.first:
                self.first = self.prev
                self.middle = root
            else:
                self.last = root
        
        self.prev = root
        
        self.inorder(root.right)
    
    def correctBST(self, root):
        # Perform inorder traversal to find swapped nodes
        self.inorder(root)
        
        # Fix swapped nodes
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data
        
        return root
