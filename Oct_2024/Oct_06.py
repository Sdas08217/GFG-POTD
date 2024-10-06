# Find the number of islands
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        # Directions for 8 possible moves (vertical, horizontal, and diagonal)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def iterative_dfs(i, j):
            # Stack for DFS
            stack = [(i, j)]
            grid[i][j] = 0  # Mark the starting land cell as visited
            
            # Perform DFS using an explicit stack
            while stack:
                x, y = stack.pop()
                
                # Explore all 8 directions
                for di, dj in directions:
                    ni, nj = x + di, y + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 0  # Mark as visited
                        stack.append((ni, nj))  # Add the land cell to stack for further exploration
        
        num_islands = 0
        
        # Iterate over every cell in the grid
        for i in range(n):
            for j in range(m):
                # If we find an unvisited land cell, start an iterative DFS
                if grid[i][j] == 1:
                    num_islands += 1
                    iterative_dfs(i, j)
        
        return num_islands

#Example Usage
# Create an instance of the Solution class
sol = Solution()

# Define the grid (as a list of lists)
grid = [
    [0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

# Call the numIslands method and print the result
result = sol.numIslands(grid)
print("Number of islands:", result)
