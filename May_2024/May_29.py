# Geek and its Game of Coins
class Solution:
    def findWinner(self, n: int, x: int, y: int) -> int:
        # Initialize dp array
        dp = [0] * (n + 1)
        
        # Base case
        dp[0] = 0  # If there are no coins left, the current player loses.
        
        # Fill the dp array
        for i in range(1, n + 1):
            # Check if the current player can force a win by picking 1, x, or y coins
            if i >= 1 and dp[i - 1] == 0:
                dp[i] = 1
            elif i >= x and dp[i - x] == 0:
                dp[i] = 1
            elif i >= y and dp[i - y] == 0:
                dp[i] = 1
            else:
                dp[i] = 0
        
        return dp[n]
      # Example usage:
if __name__ == "__main__":
    print(findWinner(5, 3, 4))  # Output: 1
    print(findWinner(2, 3, 4))  # Output: 0
