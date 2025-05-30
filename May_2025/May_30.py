class Solution:
    def findMaxFork(self, root, k):
        result = -1  # Default if no such value found
        while root:
            if root.data <= k:
                result = root.data
                root = root.right
            else:
                root = root.left
        return result
