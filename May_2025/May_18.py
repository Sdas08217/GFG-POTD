from collections import deque

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def findSpiral(self, root):
        if not root:
            return []

        result = []
        deque_nodes = deque([root])
        left_to_right = False

        while deque_nodes:
            level_size = len(deque_nodes)
            level_nodes = []

            for _ in range(level_size):
                if left_to_right:
                    node = deque_nodes.popleft()
                    level_nodes.append(node.data)
                    if node.left:
                        deque_nodes.append(node.left)
                    if node.right:
                        deque_nodes.append(node.right)
                else:
                    node = deque_nodes.pop()
                    level_nodes.append(node.data)
                    if node.right:
                        deque_nodes.appendleft(node.right)
                    if node.left:
                        deque_nodes.appendleft(node.left)

            result.extend(level_nodes)
            left_to_right = not left_to_right

        return result
