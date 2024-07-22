# Largest BST
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    def largestBst(self, root):
        def postOrder(node):
            if not node:
                return True, 0, float('inf'), float('-inf') # isBST, size, min, max

            left_is_bst, left_size, left_min, left_max = postOrder(node.left)
            right_is_bst, right_size, right_min, right_max = postOrder(node.right)

            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                current_size = left_size + right_size + 1
                return True, current_size, min(left_min, node.data), max(right_max, node.data)
            else:
                return False, max(left_size, right_size), 0, 0

        is_bst, size, min_val, max_val = postOrder(root)
        return size

# Example usage:
# Tree 1
root1 = Node(1)
root1.left = Node(4)
root1.right = Node(4)
root1.left.left = Node(6)
root1.left.right = Node(8)
solution = Solution()
print(solution.largestBst(root1))  # Output: 1

# Tree 2
root2 = Node(6)
root2.left = Node(6)
root2.right = Node(2)
root2.left.right = Node(2)
root2.right.left = Node(1)
root2.right.right = Node(3)
print(solution.largestBst(root2))  # Output: 3
