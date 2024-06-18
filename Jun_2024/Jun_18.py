# Number of Rectangles in a Circle
class Solution:
    def rectanglesInCircle(self, r):
        count = 0
        max_dim = 2 * r  # maximum possible dimension for width and height
        max_square = 4 * r * r  # precalculate 4 * r^2
        for w in range(1, max_dim + 1):
            for h in range(w, max_dim + 1):
                if w * w + h * h <= max_square:
                    count += 1
                    if w != h:
                        count += 1  # account for both (w, h) and (h, w)
                else:
                    break  # no need to check further if this condition is false
        return count

  # Example usage:
solution = Solution()
print(solution.rectanglesInCircle(1))  # Output: 1
print(solution.rectanglesInCircle(2))  # Output: 8
