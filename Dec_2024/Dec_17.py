class Solution:
    def aggressiveCows(self, stalls, k):
        # Step 1: Sort the stalls
        stalls.sort()
        
        # Step 2: Define the binary search range
        low = 1  # Minimum possible distance
        high = stalls[-1] - stalls[0]  # Maximum possible distance
        result = 0

        # Helper function to check feasibility
        def canPlaceCows(distance):
            count = 1  # Place the first cow in the first stall
            last_position = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                if count == k:
                    return True
            return False

        # Binary search for the maximum minimum distance
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(mid):
                result = mid  # Update result, as mid is feasible
                low = mid + 1  # Try for a larger distance
            else:
                high = mid - 1  # Try for a smaller distance

        return result

  # Example usage
if __name__ == "__main__":
    stalls1 = [1, 2, 4, 8, 9]
    k1 = 3
    print(Solution().aggressiveCows(stalls1, k1))  # Output: 3

    stalls2 = [10, 1, 2, 7, 5]
    k2 = 3
    print(Solution().aggressiveCows(stalls2, k2))  # Output: 4

    stalls3 = [2, 12, 11, 3, 26, 7]
    k3 = 5
    print(Solution().aggressiveCows(stalls3, k3))  # Output: 1
