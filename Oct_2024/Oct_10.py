# Linked List Matrix
class Node:
    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None
class Solution:
    def constructLinkedMatrix(self, mat):
        if not mat or not mat[0]:
            return None
        
        n = len(mat)
        
        # Create a matrix of nodes
        node_matrix = [[None for _ in range(n)] for _ in range(n)]
        
        # Step 1: Create a node for each element of the matrix
        for i in range(n):
            for j in range(n):
                node_matrix[i][j] = Node(mat[i][j])
        
        # Step 2: Link the nodes
        for i in range(n):
            for j in range(n):
                # Link the current node to the right if possible
                if j + 1 < n:
                    node_matrix[i][j].right = node_matrix[i][j + 1]
                
                # Link the current node to the down if possible
                if i + 1 < n:
                    node_matrix[i][j].down = node_matrix[i + 1][j]
        
        # Return the head node (top-left corner of the matrix)
        return node_matrix[0][0]
# Helper function to print the 2D linked list
def printLinkedMatrix(head):
    down_ptr = head
    while down_ptr:
        right_ptr = down_ptr
        while right_ptr:
            print(right_ptr.data, end=" ")
            right_ptr = right_ptr.right
        print()
        down_ptr = down_ptr.down
# Example Usage
sol = Solution()
# Test case 1
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
head = sol.constructLinkedMatrix(mat)
print("Linked List for mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:")
printLinkedMatrix(head)
# Test case 2
mat2 = [[23, 28], [23, 28]]
head2 = sol.constructLinkedMatrix(mat2)
print("\nLinked List for mat = [[23, 28], [23, 28]]:")
printLinkedMatrix(head2)
