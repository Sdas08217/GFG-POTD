# Duplicate Subtrees 
class Solution:
    def printAllDups(self, root):
        ret = {}
        seen = set()
        def dfs(cur = root):
            if not cur:
                return [-1]
            left = dfs(cur.left)
            right = dfs(cur.right)
            tmp = [cur.data] + left + right
            if tuple(tmp) in seen:
                ret[tuple(tmp)] = cur
            else:
                seen.add(tuple(tmp))
            return tmp
        dfs()
        return [ret[x] for x in sorted(ret)]

  # Define the binary tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)

# Create an instance of Solution and find duplicate subtrees
solution = Solution()
duplicates = solution.printAllDups(root)

# Print the roots of the duplicate subtrees
for node in duplicates:
    print(node.data)  # Output should be the root values of the duplicate subtrees
