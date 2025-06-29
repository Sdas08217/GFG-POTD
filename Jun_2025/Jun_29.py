class Solution:
    def splitArray(self, arr, k):
        def is_possible(max_sum):
            count = 1
            current_sum = 0
            for num in arr:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count <= k

        low = max(arr)
        high = sum(arr)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
