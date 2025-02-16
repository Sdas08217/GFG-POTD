class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        res = []
        
        # Pre-order traversal helper function.
        def preorder(node):
            if not node:
                res.append("N")  # Use "N" as a marker for None.
                return
            res.append(node.data)  # Append the node's value.
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res
    # Function to deserialize a list and construct the tree.
    def deSerialize(self, arr):
        # We'll use an iterator (or index pointer) to keep track of our position in the list.
        self.index = 0
        
        # Helper function to build tree recursively.
        def helper():
            # If we are out of elements or current element is "N", return None.
            if self.index >= len(arr) or arr[self.index] == "N":
                self.index += 1  # Move past the "N" marker.
                return None
            
            # Create a node with the current value.
            node = Node(arr[self.index])
            self.index += 1  # Move to the next element.
            node.left = helper()   # Recurse for left child.
            node.right = helper()  # Recurse for right child.
            return node
        
        return helper()
