# Merge two BST 's
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root):
        """Perform in-order traversal of a BST and return the elements in a list."""
        stack, result = [], []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.data)
            current = current.right
        return result

    def merge_sorted_lists(self, list1, list2):
        """Merge two sorted lists into one sorted list."""
        merged_list = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1
        return merged_list

    def merge(self, root1, root2):
        """Merge two BSTs and return the elements in sorted order."""
        # Get the in-order traversal of both BSTs
        sorted_list1 = self.inorder_traversal(root1)
        sorted_list2 = self.inorder_traversal(root2)
        # Merge the two sorted lists
        merged_sorted_list = self.merge_sorted_lists(sorted_list1, sorted_list2)
        return merged_sorted_list

# Function to insert nodes into the BST
def insert_into_bst(root, data):
    if not root:
        return TreeNode(data)
    if data < root.data:
        root.left = insert_into_bst(root.left, data)
    else:
        root.right = insert_into_bst(root.right, data)
    return root

# Helper function to create a BST from a list of values
def create_bst_from_list(values):
    root = None
    for value in values:
        if value != 'N':
            root = insert_into_bst(root, value)
    return root

# Example usage:
# BST1 values
bst1_values = [5, 3, 6, 2, 4]
root1 = create_bst_from_list(bst1_values)

# BST2 values
bst2_values = [2, 1, 3, 'N', 'N', 'N', 7, 6, 'N']
root2 = create_bst_from_list(bst2_values)

# Create solution instance
solution = Solution()
# Merging BST1 and BST2
merged_list = solution.merge(root1, root2)
print(merged_list)  # Output: [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]

# Another set of example BST values
# BST1 values
bst1_values = [12, 9, 6, 11]
root1 = create_bst_from_list(bst1_values)

# BST2 values
bst2_values = [8, 5, 10, 2]
root2 = create_bst_from_list(bst2_values)

# Merging BST1 and BST2
merged_list = solution.merge(root1, root2)
print(merged_list)  # Output: [2, 5, 6, 8, 9, 10, 11, 12]
