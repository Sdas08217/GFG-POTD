# Missing And Repeating
class Solution:
    def findTwoElement(self, arr): 
        n = len(arr)
        
        # Step 1: Calculate expected sum and sum of squares
        expected_sum = n * (n + 1) // 2
        expected_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

        # Step 2: Calculate actual sum and sum of squares
        actual_sum = actual_sum_of_squares = 0
        for num in arr:
            actual_sum += num
            actual_sum_of_squares += num * num

        # Step 3: Use the differences to find missing and repeating numbers
        sum_diff = expected_sum - actual_sum  # A - B
        square_sum_diff = expected_sum_of_squares - actual_sum_of_squares  # A^2 - B^2

        # A^2 - B^2 = (A - B)(A + B)
        # (A - B) is sum_diff, so we can find (A + B)
        sum_AB = square_sum_diff // sum_diff

        # Step 4: Calculate A and B
        A = (sum_AB + sum_diff) // 2
        B = sum_AB - A

        return B, A

  # Example usage
arr = [4, 3, 6, 2, 1, 1]  # The repeating element is 1, and the missing element is 5

sol = Solution()
repeating, missing = sol.findTwoElement(arr)
print(f"Repeating element: {repeating}, Missing element: {missing}")
