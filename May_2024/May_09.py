#Divisor Game
class Solution:
    def divisorGame(self, n):
        return n % 2 == 0
         # Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Test cases
    n1 = 2
    n2 = 3

    # Determine if Alice wins the game for each test case
    result1 = solution.divisorGame(n1)
    result2 = solution.divisorGame(n2)

    # Print the results
    print("Alice wins the divisor game for n =", n1, ":", result1)
    print("Alice wins the divisor game for n =", n2, ":", result2)
