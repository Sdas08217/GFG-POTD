# Binary Tree to DLL
class Solution:
     def bToDLL(self, root):

        def dfs(node):
            first = last = node
            if node.left:
                first, node.left = dfs(node.left)
                node.left.right = node
            if node.right:
                node.right, last = dfs(node.right)
                node.right.left = node
            return first, last

        return dfs(root)[0]

  # Example usage:
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    # Convert binary tree to doubly linked list
    sol = Solution()
    dll_head = sol.bToDLL(root)

    # Traverse the doubly linked list
    current = dll_head
    print("Doubly linked list from binary tree:")
    while current:
        print(current.data, end=" ")
        current = current.right
