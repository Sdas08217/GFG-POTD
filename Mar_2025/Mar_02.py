from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # Handle edge cases
        if not arr or k == 0:
            return []
        
        n = len(arr)
        if k > n:
            return []
        
        result = []  # To store the maximums of each subarray
        deq = deque()  # Deque to store indices
        
        # Process the first window of size k
        for i in range(k):
            # Remove elements smaller than arr[i] from the back
            while deq and arr[deq[-1]] < arr[i]:
                deq.pop()
            deq.append(i)
        
        # Add the maximum of the first window
        result.append(arr[deq[0]])
        
        # Process the remaining windows
        for i in range(k, n):
            # Remove indices outside the current window
            while deq and deq[0] <= i - k:
                deq.popleft()
            
            # Remove elements smaller than arr[i] from the back
            while deq and arr[deq[-1]] < arr[i]:
                deq.pop()
            
            # Add the current index
            deq.append(i)
            
            # Add the maximum of the current window
            result.append(arr[deq[0]])
        
        return result
