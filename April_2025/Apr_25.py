class Solution:
    def majorityElement(self, arr):
        # Step 1: Find a candidate for majority element
        candidate = None
        count = 0

        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Step 2: Verify if the candidate is actually the majority
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        else:
            return -1
