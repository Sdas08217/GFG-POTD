class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findPreSuc(self, root, key):
        predecessor = None
        successor = None
        
        # Find predecessor
        current = root
        while current:
            if current.data >= key:
                current = current.left
            else:
                predecessor = current
                current = current.right
        
        # Find successor
        current = root
        while current:
            if current.data <= key:
                current = current.right
            else:
                successor = current
                current = current.left
        
        return (predecessor, successor)
