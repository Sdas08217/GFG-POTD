# Check for BST
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    
    def isBSTUtil(self, node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        # Use the appropriate attribute name
        val = getattr(node, 'data', None)
        if val is None:
            val = getattr(node, 'val', None)
        
        if val is None:
            raise AttributeError("Node does not have 'data' or 'val' attribute")

        if val <= lower or val >= upper:
            return False

        if not self.isBSTUtil(node.right, val, upper):
            return False
        if not self.isBSTUtil(node.left, lower, val):
            return False

        return True

    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return self.isBSTUtil(root)

# Helper function to build the tree from the given input format
def buildTree(arr):
    if not arr or arr[0] == 'N':
        return None
    
    root = TreeNode(int(arr[0]))
    queue = [root]
    i = 1
    while queue and i < len(arr):
        current = queue.pop(0)
        
        if i < len(arr) and arr[i] != 'N':
            current.left = TreeNode(int(arr[i]))
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] != 'N':
            current.right = TreeNode(int(arr[i]))
            queue.append(current.right)
        i += 1
    
    return root

# Example Usage
input_list = [2, 1, 3, 'N', 'N', 'N', 5]
root = buildTree(input_list)
solution = Solution()
print(solution.isBST(root))  # Output: True
