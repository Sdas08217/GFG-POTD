# Bottom View of Binary Tree
from collections import deque, defaultdict

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Dictionary to store the bottom view of the nodes
        hd_node_map = defaultdict(int)
        # Queue for level order traversal
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            # Overwrite the value at horizontal distance with the current node's data
            hd_node_map[hd] = node.data
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Extract the bottom view values in sorted order of their horizontal distance
        bottom_view = [hd_node_map[hd] for hd in sorted(hd_node_map.keys())]
        return bottom_view

# Function to build tree from input string
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size = size + 1
    i = 1
    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size = size - 1

        currVal = ip[i]
        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]
        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root
  
