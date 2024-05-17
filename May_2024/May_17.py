# Find Pair Given Difference

from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        arr.sort()
        low, high = 0, 1
        
        while low < n and high < n:
            if low != high and abs(arr[high] - arr[low]) == x:
                return 1
            elif abs(arr[high] - arr[low]) < x:
                high += 1
            else:
                low += 1
                if low == high:  # Ensure high is always ahead of low
                    high += 1

        return -1

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Define test cases
    test_cases = [
        ([1, 8, 30, 40, 100], 60),  # Expected output: 1
        ([1, 2, 3, 4, 5], 6),       # Expected output: -1
        ([5, 20, 3, 2, 50, 80], 78),# Expected output: 1
        ([90, 70, 20, 80, 50], 45)  # Expected output: -1
    ]

    # Run the test cases
    for arr, x in test_cases:
        n = len(arr)
        result = solution.findPair(n, x, arr)
        print(f"Array: {arr}, x: {x} -> {'Pair found' if result == 1 else 'No pair found'}")
