#Find The Highest Number
class Solution:
    def findPeakElement(self, a):
        return max(a)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    array = [1, 2, 3, 1]
    peak_element = solution.findPeakElement(array)
    print("Peak element:", peak_element)
