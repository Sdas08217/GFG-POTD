class Solution:
    def findDuplicate(self, arr):
        # Phase 1: Detect the intersection point of two runners.
        slow = arr[0]
        fast = arr[0]
        
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (duplicate element).
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        
        return slow
