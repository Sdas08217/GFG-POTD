# Populate Inorder Successor for all nodes
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    def populateNext(self, root):
        def inorder(node):
            nonlocal prev
            if not node:
                return
            
            inorder(node.left)
            
            if prev is not None:
                prev.next = node
            
            prev = node
            
            inorder(node.right)
        
        prev = None
        
        inorder(root)

  # Example usage:
if __name__ == "__main__":
    # Constructing the binary tree
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(17)

    # Populating the next pointers
    sol = Solution()
    sol.populateNext(root)

    # Printing the in-order traversal using next pointers
    print_inorder_with_next(root)
