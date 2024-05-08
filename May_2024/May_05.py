# Vertical sum

class Solution:
    def verticalSum(self, root):
        # Dictionary to store the sum of nodes for each vertical position
        vertical_sums = {}
        # Variables to keep track of the minimum and maximum vertical positions
        min_pos, max_pos = 0, 0

        # Recursive function to calculate the vertical sum
        def calculate_vertical_sum(node, pos):
            if not node:
                return
            # Update the sum for the current vertical position
            vertical_sums[pos] = vertical_sums.get(pos, 0) + node.data
            # Update the minimum and maximum vertical positions
            nonlocal min_pos, max_pos
            min_pos = min(min_pos, pos)
            max_pos = max(max_pos, pos)
            # Recursively calculate the sum for left and right subtrees
            calculate_vertical_sum(node.left, pos - 1)
            calculate_vertical_sum(node.right, pos + 1)

        # Start the calculation with the root at vertical position 0
        calculate_vertical_sum(root, 0)

        # Return the vertical sums in the range from the minimum to maximum positions
        return [vertical_sums[i] for i in range(min_pos, max_pos + 1)]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    # Instantiate the Solution class
    solution = Solution()

    # Calculate the vertical sum
    result = solution.verticalSum(root)

    # Display the vertical sums
    print("Vertical Sums:")
    print(result)
