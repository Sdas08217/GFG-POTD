class Solution:
    def minCost(self, heights, cost):
        def get_total_cost(target_height):
            return sum(abs(h - target_height) * c for h, c in zip(heights, cost))
        
        low = min(heights)
        high = max(heights)
        answer = float('inf')

        while low <= high:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3

            cost1 = get_total_cost(mid1)
            cost2 = get_total_cost(mid2)
            answer = min(answer, cost1, cost2)

            if cost1 < cost2:
                high = mid2 - 1
            else:
                low = mid1 + 1

        return answer
