class Node:
    def __init__(self, data):  # Change val to data
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root):
        result = []
        current = root

        while current:
            if current.left is None:
                result.append(current.data)  # Change val to data
                current = current.right  # Move to the next right node
            else:
                # Find inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current  # Create thread
                    current = current.left
                else:
                    predecessor.right = None  # Revert thread
                    result.append(current.data)  # Change val to data
                    current = current.right
        
        return result

# Helper function to build a tree from level-order input
from collections import deque

def build_tree_from_level_order(data):
    if not data or data[0] is None:
        return None

    root = Node(data[0])  # Change TreeNode to Node
    queue = deque([root])
    i = 1

    while i < len(data):
        current = queue.popleft()

        if i < len(data) and data[i] is not None:
            current.left = Node(data[i])  # Change TreeNode to Node
            queue.append(current.left)
        i += 1

        if i < len(data) and data[i] is not None:
            current.right = Node(data[i])  # Change TreeNode to Node
            queue.append(current.right)
        i += 1

    return root
