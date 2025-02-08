class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        
        result = []

        # Helper function for left boundary (excluding leaf nodes)
        def leftBoundary(node):
            while node:
                if node.left or node.right:  # Exclude leaf nodes
                    result.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        # Helper function to collect leaf nodes
        def leafNodes(node):
            if not node:
                return
            leafNodes(node.left)
            if not node.left and not node.right:  # Leaf node
                result.append(node.data)
            leafNodes(node.right)

        # Helper function for right boundary (stored in reverse order)
        def rightBoundary(node):
            temp = []
            while node:
                if node.left or node.right:  # Exclude leaf nodes
                    temp.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            result.extend(temp[::-1])  # Reverse and add to result

        # Add root node **only if it is not a single node tree**
        if root.left or root.right:
            result.append(root.data)

        # Process left boundary
        if root.left:
            leftBoundary(root.left)

        # Process leaf nodes
        leafNodes(root)

        # Process right boundary
        if root.right:
            rightBoundary(root.right)

        return result


# Function to build tree from level-order input
def buildTree(arr):
    if not arr or arr[0] == 'N':
        return None

    root = Node(int(arr[0]))
    queue = [root]
    i = 1
    while queue and i < len(arr):
        currNode = queue.pop(0)
        
        # Left child
        if arr[i] != 'N':
            currNode.left = Node(int(arr[i]))
            queue.append(currNode.left)
        i += 1
        if i >= len(arr):
            break
        
        # Right child
        if arr[i] != 'N':
            currNode.right = Node(int(arr[i]))
            queue.append(currNode.right)
        i += 1
    
    return root


# Example Test Cases
test_cases = [
    (["1", "N", "N"], [1]),  # Single node
    (["1", "2", "3", "4", "5", "6", "7", "N", "N", "8", "9", "N", "N", "N", "N"], [1, 2, 4, 8, 9, 6, 7, 3]),  # Normal case
    (["1", "2", "N", "4", "9", "6", "5", "N", "3", "N", "N", "N", "N", "7", "8"], [1, 2, 4, 6, 5, 7, 8]),  # No right boundary
    (["1", "N", "2", "N", "3", "N", "4", "N", "N"], [1, 4, 3, 2])  # Right-skewed tree
]

sol = Solution()
for arr, expected in test_cases:
    root = buildTree(arr)
    output = sol.boundaryTraversal(root)
    print("Output:", output, "| Expected:", expected, "| Pass:", output == expected)
