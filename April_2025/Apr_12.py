class Solution:
    def floodFill(self, image, sr, sc, newColor):
        originalColor = image[sr][sc]
        
        # If the original color is same as newColor, no need to change
        if originalColor == newColor:
            return image

        def dfs(r, c):
            # Check if out of bounds or not the target color
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != originalColor:
                return
            
            image[r][c] = newColor  # Fill the pixel
            
            # Call dfs in 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
