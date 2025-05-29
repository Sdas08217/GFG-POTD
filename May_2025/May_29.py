class Solution:
    def sumOfLongRootToLeafPath(self, root):
        self.max_len = 0
        self.max_sum = 0

        def dfs(node, curr_len, curr_sum):
            if not node:
                return

            curr_len += 1
            curr_sum += node.data  # use .data if using custom TreeNode class

            if not node.left and not node.right:  # leaf node
                if curr_len > self.max_len:
                    self.max_len = curr_len
                    self.max_sum = curr_sum
                elif curr_len == self.max_len:
                    self.max_sum = max(self.max_sum, curr_sum)
                return

            dfs(node.left, curr_len, curr_sum)
            dfs(node.right, curr_len, curr_sum)

        dfs(root, 0, 0)
        return self.max_sum
