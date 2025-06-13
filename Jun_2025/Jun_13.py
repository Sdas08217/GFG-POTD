class Solution:
    def kokoEat(self, arr, k):
        def hours_needed(s):
            # Calculate total hours Koko needs with speed s
            return sum((pile + s - 1) // s for pile in arr)
        
        left, right = 1, max(arr)
        answer = right  # Start with the worst case

        while left <= right:
            mid = (left + right) // 2
            if hours_needed(mid) <= k:
                answer = mid  # Try to find a smaller valid s
                right = mid - 1
            else:
                left = mid + 1

        return answer
