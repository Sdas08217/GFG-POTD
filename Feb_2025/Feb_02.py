from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []  # Edge case: empty tree
        result = []
        queue = deque([root])  # Initialize queue with root
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue node
                level_nodes.append(node.data)  # Add node value to current level
                
                # Enqueue children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)  # Append current level to result
        return result
