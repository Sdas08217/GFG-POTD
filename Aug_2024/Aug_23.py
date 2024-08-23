# Left View of Binary Tree
from collections import deque

# Function to return a list containing elements of the left view of the binary tree.
def LeftView(root):
    if not root:
        return []
    
    result = []
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        
        # If this is the first node of its level
        if level == len(result):
            result.append(node.data)
        
        # Add left node to queue first
        if node.left:
            queue.append((node.left, level + 1))
        
        # Add right node to queue
        if node.right:
            queue.append((node.right, level + 1))
    
    return result

# Example Usage
# Constructing a binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#        \
#         7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.right = Node(7)

# Getting the left view of the binary tree
result = LeftView(root)
print(result)  # Output should be [1, 2, 4, 7]
