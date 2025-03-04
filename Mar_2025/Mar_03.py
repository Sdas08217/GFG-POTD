from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0
        start = 0
        
        for right in range(len(arr)):
            # Update max_deque to maintain max elements in current window
            while max_deque and arr[right] >= arr[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            # Update min_deque to maintain min elements in current window
            while min_deque and arr[right] <= arr[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            
            # Ensure the current window [left, right] is valid by adjusting left
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            
            # Update the maximum length and starting index if a longer valid subarray is found
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                start = left
        
        return arr[start:start + max_length]
