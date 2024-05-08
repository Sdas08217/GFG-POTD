# Root to Leaf Paths

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        temp = []
        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node == -1:
                temp.pop()
                continue
            temp.append(node.data)
            stack.append(-1)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not (node.left or node.right):
                ans.append(temp[:])
        return ans

  class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Let's create a binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Now, let's create an instance of Solution
solution = Solution()

# Call the Paths method to find all root-to-leaf paths
paths = solution.Paths(root)

# Print the result
print("Root-to-leaf paths:")
for path in paths:
    print(path)
