class Solution:
    # Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (include, exclude)

            left_include, left_exclude = dfs(node.left)
            right_include, right_exclude = dfs(node.right)

            # If we include current node, we can't include its children
            include = node.data + left_exclude + right_exclude

            # If we exclude current node, we can take max of including or excluding children
            exclude = max(left_include, left_exclude) + max(right_include, right_exclude)

            return (include, exclude)

        include, exclude = dfs(root)
        return max(include, exclude)
