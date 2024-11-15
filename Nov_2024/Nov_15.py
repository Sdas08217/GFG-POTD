# Second Largest.
class Solution:
    def getSecondLargest(self, arr):
        # Initialize largest and second largest with None
        largest = second_largest = -1
        for num in arr:
            # Update largest and second_largest based on current num
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest

  # Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [12, 35, 1, 10, 34, 1]
    print("Second largest element:", solution.getSecondLargest(arr))
