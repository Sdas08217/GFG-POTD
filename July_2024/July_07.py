# Ancestors in Binary Tree
def ancestors(root,target,arr):
    if(root==None):
        return False
    if(root.data==target):
        return True
    l = ancestors(root.left, target, arr)
    r = ancestors(root.right, target, arr)
    if(l or r):
        arr.append(root.data)
        
    return l or r


class Solution:

    def Ancestors(self, root, target):
        arr = []
        ancestors(root,target,arr)
        return arr

  # Example usage
if __name__ == "__main__":
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    solution = Solution()
    target = 9
    result = solution.Ancestors(root, target)
    print(f"Ancestors of node {target}: {result}")
