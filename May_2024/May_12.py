# Minimum steps to destination

class Solution:
    def minSteps(self, d):
        # code here
        for i in range(1,2* d):
            if (((i*(i+1))//2) + d)%2 == 0 and ((i*(i+1))//2) >= d:
                return i

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Test case
    d = 3

    # Calculate the minimum steps
    result = solution.minSteps(d)

    # Print the result
    print("Minimum steps required to reach", d, ":", result)
