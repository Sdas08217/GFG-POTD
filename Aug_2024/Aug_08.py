# Sum Tree
class Solution:
    def is_sum_tree(self, node):
        # Helper function that returns a tuple (is_sum_tree, sum)
        def check_sum_tree(node):
            if node is None:
                return True, 0

            if node.left is None and node.right is None:
                return True, node.data

            left_is_sum_tree, left_sum = check_sum_tree(node.left)
            right_is_sum_tree, right_sum = check_sum_tree(node.right)

            # Check if current node is sum tree
            current_is_sum_tree = (left_is_sum_tree and right_is_sum_tree and 
                                   node.data == left_sum + right_sum)

            # Return whether this subtree is a sum tree and the sum of this subtree
            return current_is_sum_tree, left_sum + right_sum + node.data

        # Only need the boolean result from the helper function
        is_sum_tree, _ = check_sum_tree(node)
        return is_sum_tree

  # Example usage
if __name__ == "__main__":
    # Constructing a tree:
    #         26
    #        /  \
    #      10    3
    #     /  \    \
    #    4    6    3

    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    solution = Solution()
    print(solution.is_sum_tree(root))  # Output: True
