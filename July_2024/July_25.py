# Array to BST
class Solution:
    def sortedArrayToBST(self, nums):
        n = len(nums)
        def mergeTree(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = Node(nums[m])
            root.left = mergeTree(l, m - 1)
            root.right = mergeTree(m + 1, r)

            return root

        return mergeTree(0, n - 1)

# Example usage
nums = [-10, -3, 0, 5, 9]
solution = Solution()
bst_root = solution.sortedArrayToBST(nums)

# Print the preorder traversal of the BST
print(preorderTraversal(bst_root))
