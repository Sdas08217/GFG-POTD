from collections import defaultdict

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def sumK(self, root, k):
        def dfs(node, currentSum):
            if not node:
                return 0
            
            # Update the current prefix sum
            currentSum += node.data  # FIX: Changed `node.val` to `node.data`
            
            # Count paths that sum to k
            count = prefixSum[currentSum - k]
            
            # Update prefix sum count
            prefixSum[currentSum] += 1
            
            # Recur for left and right subtrees
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)
            
            # Backtrack: Remove the current sum from the hashmap
            prefixSum[currentSum] -= 1
            
            return count

        # HashMap to store prefix sums
        prefixSum = defaultdict(int)
        prefixSum[0] = 1  # Base case for when the path itself equals k
        
        return dfs(root, 0)
