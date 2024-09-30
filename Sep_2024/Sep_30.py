# Merge two BST 's
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        '''Perform in-order traversal and return sorted elements as a list.'''
        result = []
        stack = []
        current = root
        
        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
                
            # Process the node
            current = stack.pop()
            result.append(current.data)  # Access 'data' instead of 'val'
            
            # Go to the right node
            current = current.right
        
        return result
    
    def mergeSortedArrays(self, arr1, arr2):
        '''Merge two sorted arrays into one sorted array.'''
        i, j = 0, 0
        merged = []
        
        # Merge two arrays
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
                
        # If there are remaining elements in arr1
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
            
        # If there are remaining elements in arr2
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
            
        return merged
    
    def merge(self, root1, root2):
        '''Return the elements of two merged BSTs in sorted form.'''
        # Perform in-order traversal to get the sorted elements of both BSTs
        arr1 = self.inorderTraversal(root1)
        arr2 = self.inorderTraversal(root2)
        
        # Merge the two sorted arrays
        return self.mergeSortedArrays(arr1, arr2)

#Example usage
# Define the trees
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

# Create an instance of Solution and merge the trees
sol = Solution()
merged_result = sol.merge(root1, root2)

# Output the merged sorted elements
print("Merged Sorted Elements:", merged_result)
