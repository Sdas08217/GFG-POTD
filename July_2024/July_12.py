# Root to leaf path sum
class Solution:

    def hasPathSum(self, root, target):
        
        def f(root,s):
            
            if not root:
                return
            
            s += root.data
            
            if s == target and not root.left and not root.right:
                return True
                
            if s != target and (not root.left and not root.right):
                return False
            
            l = f(root.left,s)
            r = f(root.right,s)
            
            return l or r
                
        return f(root,0)

  # Example usage:
# Constructing the tree: 1
#                       / \
#                      2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
print(sol.hasPathSum(root, 2))  # Output: False
print(sol.hasPathSum(root, 4))  # Output: True
