from collections import deque

class Solution:
    def mapParents(self, root, target):
        parent_map = {}
        target_node = None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.data == target:
                target_node = node
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
        return parent_map, target_node

    def burnTree(self, target_node, parent_map):
        visited = set()
        queue = deque()
        queue.append(target_node)
        visited.add(target_node)
        time = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent_map.get(node)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            time += 1
        return time

    def minTime(self, root, target):
        parent_map, target_node = self.mapParents(root, target)
        return self.burnTree(target_node, parent_map)
