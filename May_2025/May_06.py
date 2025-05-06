from collections import deque

class Solution:
    def LeftView(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                # capture the first node of each level
                if i == 0:
                    result.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
