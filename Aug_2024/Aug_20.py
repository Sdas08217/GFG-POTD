# Burning Tree
from collections import defaultdict, deque

class Solution:
    def minTime(self, root, target):
        if not root:
            return 0
        
        # Step 1: Create the graph connections
        parent_map = {}
        self.target_node = None
        
        def create_parent_map(node, parent=None):
            if node:
                parent_map[node] = parent
                if node.data == target:
                    self.target_node = node
                create_parent_map(node.left, node)
                create_parent_map(node.right, node)
        
        create_parent_map(root)
        
        # Step 2: Perform BFS from the target node
        queue = deque([(self.target_node, 0)])
        visited = set([self.target_node])
        max_time = 0
        
        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            
            # Check all connected nodes (left, right, parent)
            for neighbor in (node.left, node.right, parent_map.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, time + 1))
        
        return max_time

  # Example Input:
values = [1, 2, 3, 4, 5, 'N', 6, 'N', 'N', 7, 8, 'N', 9, 10, 11, 'N', 'N', 'N', 12, 'N', 'N', 'N', 13]
target = 8

# Build the tree
root = build_tree(values)

# Create a Solution object and find the minimum time
solution = Solution()
print(solution.minTime(root, target))  # Expected Output: 7
