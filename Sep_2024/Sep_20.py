# Facing the sun
class Solution:
    # Returns count of buildings that can see sunlight
    def countBuildings(self, height):
        if not height:
            return 0

        # Initialize the count and the maximum height seen so far
        count = 1  # First building always sees the sunrise
        max_height = height[0]

        # Iterate through the list starting from the second building
        for i in range(1, len(height)):
            if height[i] > max_height:
                count += 1
                max_height = height[i]

        return count

  # Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example list of building heights
    heights = [7, 4, 8, 5, 3, 9, 6]
    
    # Counting buildings that can see the sunrise
    result = solution.countBuildings(heights)
    print(f"Number of buildings that can see the sunrise: {result}")
